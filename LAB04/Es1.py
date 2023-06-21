import cherrypy
import json
import time

class myWebService:
    exposed = True
            
    def GET(self,*uri):
        
        message={}
        if len(uri) == 0:
            return "Welcome to my REST web page\nYou can use as URI /temperature, /humidity, /allSensor "
        else:
            if uri[0] == "temperature":
                message=self.getMessage(0)
                return json.dumps(message,indent=4) 
            elif uri[0] == "humidity":
                message = self.getMessage(1)
                return json.dumps(message,indent=4)
            elif uri[0] == "allSensor":
                message = self.getMessage(2)
                return json.dumps(message,indent=4)
            else:
                return "Error, bad request"
            

    def getMessage(self, param):
        completeMessage = json.load(open("sensorValues.json"))
        messageToReturn = {}
        topic = completeMessage["sensorID"]
        message = completeMessage["message"]
        msg = ""

        if param == 0:
            msg = message['e'][0]
        elif param == 1:
            msg = message['e'][1]
            
        elif param == 2:
            msg = []
            msg = message['e']

        messageToReturn["bn"] = topic
        messageToReturn["e"] = msg

        return messageToReturn
        
if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    time.sleep(10)
    cherrypy.tree.mount(myWebService(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()