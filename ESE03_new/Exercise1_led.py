from mySubscriber import *
import time
import json

class Led:
    """Led is an instance of MQTT subscriber. It receives the command from a publisher in order to set On/Off status"""
    def __init__(self, clientID):
        self.sub=MySubscriber(clientID,self)
        self.status= "Off"
        
    def notify(self,topic,payload):
        msg=json.loads(payload)
        print("Received message:\n\t "+ msg["status"])
        if msg["status"] == "On" or msg["status"] == "on":
            self.status = "On"
        elif msg["status"] == "Off" or msg["status"] == "off":
            self.status = "Off"
        elif msg["status"] == "Exit" or msg["status"] == "exit" :
            self.status = "Exit"
        else:
            print("Error: Bad request!")
        return
    
    def startConnection(self):
        baseTopic = self.sub.setup()
        self.sub.connect()
        self.sub.subscribeToTopic(baseTopic,2)
    
    def subscribeToNewTopic(self, newTopic):
        self.sub.subscribeToTopic(newTopic,2)
        
    def stopConnection(self):
        self.sub.disconnect()
        
    def getStatus(self):
        return self.status
    
if __name__ == '__main__':
    led1 = Led("user1234")
    led1.startConnection()
    led1.subscribeToNewTopic("IoT/Omar/led")
    a = 0
    exitFlag = 0 ##added to force exit after 20 times
    
    print("Hello LED")
    
    while a == 0:
        exitFlag +=1 ##added to force exit after 20 times
        if led1.getStatus() == "Exit" or exitFlag > 15: 
            a = 1
        else: 
            print("\tLed status is " + led1.getStatus())
        time.sleep(10)
    
    led1.stopConnection()
    
    
    
    

