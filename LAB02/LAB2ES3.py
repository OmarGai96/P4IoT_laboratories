###MAIN CLASS
import cherrypy
import json
from CalculatorExt import *



class myWebService:
    
    exposed = True

    def __init__(self):
        pass

    def PUT(self,*uri,**query):
        calc=CalculatorExt()
        myDict = json.loads(cherrypy.request.body.read())  ##read the body of the PUT method
        result=calc.computeExt(myDict['command'],myDict['operands'])
        if result != "":
            myDict['result'] = result
            return json.dumps(myDict)
        else:
            return "Operation Failed"

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

    

    
