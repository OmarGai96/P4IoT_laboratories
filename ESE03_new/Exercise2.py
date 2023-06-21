import cherrypy
import json

from myPublisher import *
import time

class actuator:
    """Actuator is an instance of MQTT publisher. It sends command to a Led in order to set On/Off status"""
    def __init__(self, clientID):
        self.pub=MyPublisher(clientID,self)
        self.clientID = clientID
    
    def startConnection(self):
        self.pub.setup()
        self.pub.connect()
        
    def stopConnection(self):
        self.pub.disconnect()
        
    def publish(self,topic,msg,Qos):
        self.pub.publish(topic,msg,Qos)
        
    def getClientID(self):
        return self.clientID

class myWebService:
    
    def __init__(self):
        self.switch = actuator("user5678")
        self.switch.startConnection()
        
    def exit(self):
        self.switch.stopConnection()
    
    exposed = True
    def GET (self, *uri, **params):
        if len(uri) ==0:
            return open('./index.html','r').read()
        elif len(uri) == 1:
            if uri[0]=='exit':
                self.exit()
                return "Exit"
        else:
            raise cherrypy.HTTPError(400, "Bad request: wrong command")

    def PUT (self, *uri):
        msgToSend = {}
        msgToSend["bn"] = self.switch.getClientID()
        if len(uri) == 1:
            if uri[0] == "on" or uri[0] == "off" or uri[0] == "On" or uri[0] == "Off":
                msgToSend["status"] = uri[0]
                self.switch.publish("IoT/Omar/led",msgToSend,2)
            else:
                print("Bad request, please retransmit")
                return "Bad request, please retransmit"
        else:
            raise cherrypy.HTTPError(400, "Bad request: wrong command")


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
 

    
    