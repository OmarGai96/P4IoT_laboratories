import cherrypy
class UriReverser():

    exposed = True

    def GET(self, *uri):
        if len(uri) !=0:
            return ', '.join([str(x)[::-1] for x in uri])
            ##comma is used to separate elements, x is used to store elements (uris)
        else:
            # you can define a simple http error message
            raise cherrypy.HTTPError(400, 'No URI given, you need to provide at least one uri')
            

if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    cherrypy.tree.mount(UriReverser(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
