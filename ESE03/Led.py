from MyMQTT import *
import json

##subscriber side --> LED
class Led():
    def __init__(self, clientId,broker,port,topic):
        self.clientId = clientId;
        self.status ='off'
        self.mqttClient=MyMQTT(clientId,broker,port,self)  #self is for the notifier
        self.topic=topic

    def notify(self,topic,payload):
        msg=json.loads(payload)
        self.status=msg['status'] #payload is a dictionary
        print(f"\t\tClientId: {msg['bn']}")
        print(f"\t\tLed is {self.status}")

    def startSim(self):        
        self.mqttClient.start()
        self.mqttClient.mySubscribe(self.topic)
        print(f"Starting Led status: {self.status}\n")

    def myUnsubscribe(self):
        self.mqttClient.unsubscribe()

    def stopSim(self):
        self.mqttClient.stop()

    def sendMessage(self, msg):
        msgToSend = {}
        msgToSend["bn"] = self.clientId
        if msg == 'on' and self.status == 'off':   
            msgToSend["status"] = msg
            self.mqttClient.myPublish(self.topic, msgToSend)
        elif msg == 'off' and self.status == 'on': 
            msgToSend["status"] = msg
            self.mqttClient.myPublish(self.topic, msgToSend)
        else:
            print(f"Message not send, led is {msg} yet\n")
