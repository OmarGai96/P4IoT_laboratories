import paho.mqtt.client as PahoMQTT
import json

class MyPublisher():

    def __init__(self, clientID, notifier):
        self.clientID = clientID
        self.subscriber = ""
        self.settings = {}
        self.topic = ""
        self.broker = ""
        self.port = -1
        self.notifier = notifier
        self._isSubscriber = False
        
        return
    
    #This function reads setting parameters from a file and performs an initial setup for subscriber    
    def setup(self, filename):
        self.settings = json.load(open(filename, "r"))
        self.topic = self.settings["baseTopic"]
        self.broker = self.settings["broker"]
        self.port = self.settings["port"]
    
        self._paho_mqtt = PahoMQTT.Client(self.clientID, True) #FAlse means the client is a  durable client
                                                                #TRUE = transient connection
        # register the callback
        self._paho_mqtt.on_connect = self.myOnConnect

    def connect(self):
	    #manage connection to broker
        self._paho_mqtt.connect(self.broker , self.port) #arguments are hostname of the remote broker and network port of the server (1883)
        self._paho_mqtt.loop_start()    #network loop start  
    
    def publish(self, topic, msg, QoS):
        # if needed, you can do some computation or error-check before subscribing
        msgToSend = json.dumps(msg)
        print ("publishing message with topic '%s'" % (topic))
        self._paho_mqtt.publish(topic, msgToSend, int(QoS)) #arguments are msg, topic and QoS
        
    def disconnect(self):
		# remember to unsuscribe if it is working also as subscriber 
        self._paho_mqtt.loop_stop()     #network loop stop        
        self._paho_mqtt.disconnect()    #disconnects from the broker cleanly
    
    def myOnConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to %s with result code: %d" % (self.broker, rc))

    
#####################################################################    

    def getTopic(self):
        return self.topic