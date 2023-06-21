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
    
if __name__ == '__main__':
    switch = actuator("user5678")
    switch.startConnection()
    msgToSend = {}
    msgToSend["bn"] = switch.getClientID()
    a = 0
    
    while a == 0:
        msg=input("Turn On or Off led (type 'exit' to close): ")
        if msg == "exit" or msg == "Exit":
            a = 1
        elif msg == "on" or msg == "On" or msg == "off" or msg == "Off":
            msgToSend["status"] = msg
            switch.publish("IoT/Omar/led",msgToSend,2)
        else: 
            print("Bad request, please retransmit")
    switch.stopConnection()
    