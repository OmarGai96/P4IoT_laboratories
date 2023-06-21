import cherrypy
import json

class MyWebService(object):
    exposed=True
    def GET (self,**param):
        out = ''
        if len(param)!=0:
            return 'reversed values of param dict: ' + ''.join(str(json.dumps({key:param[key][::-1] for key in param})))

if __name__ == '__main__':
    conf={
        '/':{
                'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on':True
        }
    }
    cherrypy.tree.mount(MyWebService(),'/',conf)
    cherrypy.config.update(conf)
    cherrypy.config.update({"server.socket_port" : 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
