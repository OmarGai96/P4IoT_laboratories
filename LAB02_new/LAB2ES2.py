import cherrypy
import json
from Calculator import *

class myWebService:
    
    exposed = True
    def GET (self, *uri, **params):
        calc = Calculator("webServCalc")
        if len(uri) != 3:
            raise cherrypy.HTTPError(400, "Bad request: wrong command")
        else:
            res = calc.calculate(uri[0],int(uri[1]), int(uri[2]))
            if res == "wrong operation":
                raise cherrypy.HTTPError(400, "Bad request: Wrong operation")
            
            elif res == "null":
                raise cherrypy.HTTPError(400, "Bad request: DivException occurred")
            
            else:
                newDict = {}
                newDict["operation"] = uri[0]
                newDict["op1"]= uri[1]
                newDict["op2"]= uri[2]
                newDict["result"]= res
                return json.dumps(newDict)
                

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
    
    