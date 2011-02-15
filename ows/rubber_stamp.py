import cherrypy
import json  # requires relatively new python, otherwise simple_json

class JsonResponse(object):
    """Sends JSON data to hookbox callbacks."""
    def __init__(self,data):
        self.data = data

    def index(self):
        return json.dumps( self.data )
    index.exposed = True


class RubberStamp(object):
    """Approves all hookbox authentication requests.
    The most simple way to get hookbox working.
    """

    def index(self):
        return "Rubber stamp for hookbox auth"
    index.exposed = True

    true_response = [ True, {} ]

    connect = JsonResponse( true_response )
    disconnect = JsonResponse( true_response )
    subscribe = JsonResponse( true_response )
    unsubscribe = JsonResponse( true_response )
    publish = JsonResponse( true_response )

    # See: http://hookbox.org/docs/javascript.html#channel-attributes
    channel_attrib = [ True, { "history_size" : 0, 
                               "reflective" : True, 
                               "presenceful" : True } ]
    create_channel = JsonResponse( channel_attrib )


cherrypy.quickstart(RubberStamp())

