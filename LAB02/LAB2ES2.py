###MAIN CLASS
import cherrypy
import json
from Calculator import *



class myWebService:
    
    exposed = True

    def __init__(self):
        pass
    
    def GET(self,*uri):  ##uri is the operation, params are the operands
        calc=Calculator()
        toReturn=""
        myOperation={}
        if len(uri)==3:
            oper = uri[0]
            op1=int(uri[1])
            op2=int(uri[2])
            result = calc.compute(oper,op1,op2)
            self.printJSON(oper,op1,op2,result)
            if result=="":
                return "OperationFailed"
            else:
                myOperation={"operation": oper, "operand_1": op1,"operand_2": op2, "result": result}
                return json.dumps(myOperation)     
        else: 
            return "Uri lenght is wrong"
        
    def printJSON(self,operation,a,b,c):
        f=open("result.json", "w")
        if c == "":
            f.write("Operation failed")
        else:
            f.write("{")
            f.write(f'\n\t"operation": "{operation}",')
            f.write(f'\n\t"operand_1": {a},')
            f.write(f'\n\t"operand_2": {b},')
            f.write(f'\n\t"result"   : {c} ')
            f.write("\n}") 
        f.close() 
        return

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

    

    
