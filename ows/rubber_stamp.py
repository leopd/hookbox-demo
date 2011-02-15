import cherrypy
import json  # requires relatively new python, otherwise simple_json


def json_response(data):
    """Returns the data as json
    """
    return json.dumps(data)


class RespondTrue(object):
    """Basic response to many Hookbox callbacks.
    """
    def index(self):
        return json_response([ True, {} ])
    index.exposed = True
    

class RubberStamp(object):
    """Approves all hookbox authentication requests.
    The most simple way to get hookbox working.
    """

    def index(self):
        return "Rubber stamp for hookbox auth"
    index.exposed = True

    connect = RespondTrue()
    disconnect = RespondTrue()
    create_channel = RespondTrue()
    subscribe = RespondTrue()
    unsubscribe = RespondTrue()
    publish = RespondTrue()


cherrypy.quickstart(RubberStamp())

