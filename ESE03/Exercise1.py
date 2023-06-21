from Led import *
import time

if __name__ == '__main__':
    clientID = '1234'
    broker = "test.mosquitto.org"
    port= 1883
    topic="IoT/Omar/led"

    l = Led(clientID,broker,port,topic)

    l.startSim()
    time.sleep(2)
    
    i=0
    while i < 20:
        print('valid inputs: on, off, stop')
        status = input("Insert status of the LED: ")
        if status == 'stop':
           l.stopSim()
        elif status == 'on' or status == 'off':
            l.sendMessage(status)
            time.sleep(3)
        else:
            print("Input is not valid")
        i = i+1

    l.stopSim()
