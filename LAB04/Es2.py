import json
from mySubscriber import *
import time

class Receiver:
    
    def __init__(self):
        self.subscriber = MySubscriber("5678",self)
        self.baseTopic = self.subscriber.setup()
        
    def getBaseTopic(self):
        return self.baseTopic
    
    def start(self):
        self.subscriber.connect()
        
    def stop(self):
        self.subscriber.disconnect()
    
    def receiveMessage(self, param):
        topic = self.getBaseTopic()+"/sensor1/"+param
        if param == "temperature" or param == "humidity" or param == "allSensor":
            self.subscriber.subscribeToTopic(topic,2)
        else:
            print(f"Error, topic {topic} is wrong because '{param}' is not supported")
            
    def notify(self,topic,payload):
        msg = json.loads(payload)
        bn = msg["bn"].split("/")
        identifier = str(bn[0])+str(bn[1])
        param = str(bn[2])
        if param == "allSensor":
            e = msg['e']
            val = e[0]
            n = val['n']
            u = val['u']
            v = str(val['v'])
            t = str(val['t'])
            print(f"{identifier} measured a {n} of {v} {u} at the time {t}") 
            val = e[1]
            n = val['n']
            u = val['u']
            v = str(val['v'])
            t = str(val['t'])
            print(f"{identifier} measured a {n} of {v} {u} at the time {t}") 
        else: 
            e = msg['e']
            val = e[0]
            n = val['n']
            u = val['u']
            v = str(val['v'])
            t = str(val['t'])
            print(f"{identifier} measured a {n} of {v} {u} at the time {t}")        
        
if __name__ == '__main__':
    receiver = Receiver()
    receiver.start()
    while True:
        print("Available informations: 'temperature', 'humidity', 'allSensor', 'exit'")
        t = input("What info retreive: ")
        if t == "exit":
            break
        else:
            receiver.receiveMessage(t)
            time.sleep(10)
    
    receiver.stop()