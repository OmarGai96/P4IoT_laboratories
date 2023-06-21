import cherrypy
import json

# Return the reverted parameters as JSON formatted string
class ParamsReverser(object):
    """docstring for Reverser"""
    exposed = True

    def __init__(self):
        pass

    def GET(self, *uri, **params):
        if len(uri) == 0:
            reverse = {}
            for key in params.keys():
                reverse[key] = params[key][::-1]
            return json.dumps(reverse)  #returns a string
        else:
            raise cherrypy.HTTPError(400, 'No URI given, you need to provide at least one uri')

if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    cherrypy.tree.mount(ParamsReverser(), '/simple', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()
