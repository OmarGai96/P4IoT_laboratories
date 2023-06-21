from MyMQTT import *
from Led import *
from myREST import *
import cherrypy
import json
import time

if __name__ == '__main__':

    clientID = '1234'
    broker = "test.mosquitto.org"
    port= 1883
    topic="IoT/Omar/led"

    l = Led(clientID,broker,port,topic)

    l.startSim()
    time.sleep(2)
    oldStatus = 'off'

    i = 0
    while i  < 100:
        myDict = json.load(open("req.json"))
        status = myDict['req']
        if status == 'on' and oldStatus == 'off':
            l.sendMessage(status)
            oldStatus = status
        elif status == 'off' and oldStatus == 'on':
            l.sendMessage(status)
            oldStatus = status
        time.sleep(5)
        i = i+1
