from MyMQTT import *
import json
import time

##subscriber side (Exercise3)
class Subscriber():
    def __init__(self, clientId,broker,port,topic):
        self.clientId = clientId;
        self.mqttClient=MyMQTT(clientId,broker,port,self)  #self is for the notifier
        self.topic=topic

    def notify(self,topic,payload):
        msg=json.loads(payload)
        print('Message Received')
        print(json.dumps(msg,indent=4))

    def startSim(self):        
        self.mqttClient.start()
        self.mqttClient.mySubscribe(self.topic)

    def myUnsubscribe(self):
        self.mqttClient.unsubscribe()

    def stopSim(self):
        self.mqttClient.stop()
        
    def setTopic(self, topic):
        self.mqttClient.mySubscribe(topic)

if __name__ == '__main__':

    conf=json.load(open("settings.json"))
    broker=conf["broker"]
    port=conf["port"]
    building=conf["baseTopic"]
    topic = ''
    clientSub=Subscriber('1234',broker,port,building)
    floorID = ''
    roomID = ''
    sensorID = ''
    print(f'Welcome in the building {building}')
    print('3 options to retrieve data')
    print('\topt1: all the sensors of the building')
    print('\topt2: all the sensor on a single floor')
    print('\topt3: sensor of a single room')
    flag = True
    clientSub.startSim()
    time.sleep(2)
    while (flag):
        opt = int(input('\n\nChoose option (-1 to exit): '))
        topic = ''
        if opt == 1:
            floorID = '#'
            topic = building+'/'+floorID
            clientSub.myUnsubscribe()
            clientSub.setTopic(topic) #set new topic and subscription
        elif opt == 2:
            floorID = int(input('\tChoose floor [0-4]: '))
            roomID = '#'
            if floorID>=0 and floorID<=4:
                topic = building+'/'+str(floorID)+'/'+roomID
                clientSub.myUnsubscribe()
                clientSub.setTopic(topic) #set new topic and subscription
            else:
                print('floor not valid')
        elif opt == 3:
            floorID = int(input('\tChoose floor [0-4]: '))
            roomID =  int(input('\tChoose room  [1-3]: '))
            sensorID = '+'
            if floorID>=0 and floorID<=4 and roomID>=1 and roomID<=3:
                topic = building+'/'+str(floorID)+'/'+str(roomID)+'/'+sensorID
                clientSub.myUnsubscribe()
                clientSub.setTopic(topic) #set new topic and subscription
            else:
                print('floor/room not valid')
        elif opt == -1:
            flag = False
        else:
            print('Input not valid')
        time.sleep(7)
    clientSub.myUnsubscribe()
    clientSub.stopSim()

