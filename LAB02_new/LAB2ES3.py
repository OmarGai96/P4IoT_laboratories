from CalculatorExt import *
import cherrypy
import json

class myWebService:
    
    exposed = True
        
    def PUT (self,*uri, **params):
        myCalculatorExt = CalculatorExt("myExt")
        if len(uri) != 0:
            raise cherrypy.HTTPError(400, "Bad request: wrong command")
        
        bodyContent = json.loads(cherrypy.request.body.read())
        res = myCalculatorExt.compute(bodyContent["command"], list(bodyContent["operands"]))
        
        if res == "wrong operation":
            raise cherrypy.HTTPError(400, "Bad request: Wrong operation")
            
        elif res == "null":
            raise cherrypy.HTTPError(400, "Bad request: DivException occurred")

        else:
                bodyContent["result"]= res
                return json.dumps(bodyContent)
        
if __name__=="__main__":

    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on':True
        }
    }
    
    cherrypy.tree.mount(myWebService(),'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
    