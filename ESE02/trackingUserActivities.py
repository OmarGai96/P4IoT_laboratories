import cherrypy
import json

# Return the reverted parameters as JSON formatted string
class ParamsReverser(object):
    """docstring for Reverser"""
    exposed = True
    def __init__(self):
        pass

    def GET(self, *uri, **params):
        savedString = params.values()
        if len(uri) == 1:
            return str(cherrypy.session['myString'])
        else:
            cherrypy.session['myString']=savedString
            return savedString

if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(ParamsReverser(), '/', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()
