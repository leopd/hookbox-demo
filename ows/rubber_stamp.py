import cherrypy
import json  # requires relatively new python, otherwise simple_json

class JsonResponse(object):
    """Sends JSON data to hookbox callbacks."""
    def __init__(self,data):
        self.data = data

    def index(self, *args, **kwargs):
        return json.dumps( self.data )
    index.exposed = True



class RubberStamp(object):
    """Approves all hookbox authentication requests.
    The most simple way to get hookbox working.
    """

    def __init__(self):
        self.user_number = 0

    _cp_config = {'tools.trailing_slash.on': False}
    def index(self):
        return "yes"
    index.exposed = True


    def connect(self, *args, **kwargs):
        self.user_number += 1
        name = "User %d" % self.user_number
        return json.dumps( [True, {"name":name}] )
    connect.exposed = True

    true_response = [ True, {} ]
    disconnect = JsonResponse( true_response )
    subscribe = JsonResponse( true_response )
    unsubscribe = JsonResponse( true_response )
    publish = JsonResponse( true_response )

    # See: http://hookbox.org/docs/javascript.html#channel-attributes
    channel_attrib = [ True, { "history_size" : 0, 
                               "reflective" : True, 
                               "presenceful" : True } ]
    create_channel = JsonResponse( channel_attrib )

class Root(object):
    hookbox = RubberStamp()
    hookbox.exposed = True


cherrypy.quickstart(Root())

