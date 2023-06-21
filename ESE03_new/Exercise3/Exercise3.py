import time
from mySubscriber import *

class Display:
    """Display is an instance of MQTT subscriber. It can show info received from sensors placed in a building"""
    def __init__(self, clientID):
        self.sub=MySubscriber(clientID,self)
        self.clientID = clientID
        self.baseTopic = ""
        
    def notify(self,topic,payload):
        msg=json.loads(payload)
        print("Received message from sensor dht_"+ msg["bn"])
        print(msg["e"])
        return
    
    def startConnection(self):
        self.baseTopic = self.sub.setup()
        self.sub.connect()
    
    def subscribeToNewTopic(self, newTopic):
        self.sub.subscribeToTopic(newTopic,2)
        
    def stopConnection(self):
        self.sub.disconnect()
    
    def getBuildingID(self):
        return self.baseTopic
    
    def stopConnectionTemp(self):
        self.sub.unsubscribe()
        return
    
if __name__ == '__main__':
    
    display = Display("display1234")
    display.startConnection()
    
    flag = 0
    
    print("Welcome in "+ display.getBuildingID())
    
    while flag == 0:
        #buildingID/floorID/roomID/sensorID
        #Iot_project/2/3/dht_11
        print("List of available options")
        print("1) Retrieve Data from all the sensors of the building")
        print("2) Retrieve Data from all the sensors on a single floor")
        print("3) Retrieve Data from the sensor in a single room")
        print("4) Exit")
        n = int(input("Select option: "))
        newTopic = ""
        
        if n == 1:
            newTopic = display.getBuildingID()+"/#"
            display.subscribeToNewTopic(newTopic)
        elif n == 2:
            floorID = input("\tSelect floor: ")
            newTopic = display.getBuildingID()+"/"+floorID+"/#"
            display.subscribeToNewTopic(newTopic)
        elif n == 3:
            floorID = input("\tSelect floor: ")
            roomID = input("\tSelect room: ")
            newTopic = display.getBuildingID()+"/"+floorID+"/"+roomID+"/#"
            display.subscribeToNewTopic(newTopic)
        elif n == 4:
            flag = 1
        else:
            print("Bad request, retry")
            
        print("\n\n")
        time.sleep(10)
        display.stopConnectionTemp() #useful to unsubscribe temporarily 
        
    display.stopConnection()