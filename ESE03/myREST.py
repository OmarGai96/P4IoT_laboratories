import cherrypy
import json

class myWebService():
    def __init__(self):
            f=open("req.json", 'w')
            f.write("{")
            f.write(f'\n\t"req": "none"')
            f.write("\n}")
            f.close()

    exposed = True

    def GET(self, *uri):
        if len(uri) == 0:

            return open('./index.html', 'r').read()
            

    def PUT(self,*uri):
        myReq = uri[0]
        print(f"My req is: {myReq}")
        print(f"body is: {cherrypy.request.body.read()}")
        f=open("req.json", 'w')
        f.write("{")
        f.write(f'\n\t"req": "{myReq}"')
        f.write("\n}")
        f.close()

if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    cherrypy.tree.mount(myWebService(), '/', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()
