import cherrypy
import json
from Calculator import *

class myWebService:
    
    exposed = True
    def GET (self, *uri, **params):
        calc = Calculator("webServCalc")
        if len(uri) ==0:
            raise cherrypy.HTTPError(400, "Bad request: wrong command")
        else:
            keys = list(params.keys())
            if keys[0] != "op1":
                raise cherrypy.HTTPError(400, "Bad request: wrong command")
            if keys[1] != "op2":
                raise cherrypy.HTTPError(400, "Bad request: wrong command")
            if params["op1"] == "" or params["op2"] == "":
                raise cherrypy.HTTPError(400, "Bad request: Wrong operator")
            res = calc.calculate(uri[0],int(params["op1"]), int(params["op2"]))
            if res == "null":
                raise cherrypy.HTTPError(400, "Bad request: DivException occurred")
            elif res == "wrong operation":
                raise cherrypy.HTTPError(400, "Bad request: Wrong operation")
            else:
                newDict = {}
                newDict["operation"] = uri[0]
                newDict["op1"]= params["op1"]
                newDict["op2"]= params["op2"]
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
    
    