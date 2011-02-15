import cherrypy
import json  # requires relatively new python, otherwise simple_json



class JsonResponse(object):
    """Basic response to many Hookbox callbacks.
    """
    def __init__(self,data):
        self.data = data

    def index(self):
        return json.dumps( self.data )
    index.exposed = True


class RespondTrue(JsonResponse):
    def __init__(self):
        true_response = [ True, {} ]
        super(RespondTrue,self).__init__( true_response )



class RubberStamp(object):
    """Approves all hookbox authentication requests.
    The most simple way to get hookbox working.
    """

    def index(self):
        return "Rubber stamp for hookbox auth"
    index.exposed = True

    connect = RespondTrue()
    disconnect = RespondTrue()
    subscribe = RespondTrue()
    unsubscribe = RespondTrue()
    publish = RespondTrue()

    channel_config = [ True, { "history_size" : 0, 
                               "reflective" : True, 
                               "presenceful" : True } ]
    create_channel = JsonResponse( channel_config )


cherrypy.quickstart(RubberStamp())

