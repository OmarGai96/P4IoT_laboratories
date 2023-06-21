import paho.mqtt.client as PahoMQTT
import json

class MySubscriber():

    def __init__(self, clientID, notifier):
        self.clientID = clientID
        self.subscriber = ""
        self.settings = {}
        self.topic = ""
        self.broker = ""
        self.port = -1
        self.notifier = notifier
        self._isSubscriber = True
        
        return
    
    #This function reads setting parameters from a file and performs an initial setup for subscriber    
    def setup(self):
        self.settings = json.load(open("settings.json", "r"))
        self.topic = self.settings["baseTopic"]
        self.broker = self.settings["broker"]
        self.port = self.settings["port"]
    
        self._paho_mqtt = PahoMQTT.Client(self.clientID, True) #FAlse means the client is a  durable client
                                                                #TRUE = transient connection
        # register the callback
        self._paho_mqtt.on_connect = self.myOnConnect
        self._paho_mqtt.on_message = self.myOnMessageReceived
        return self.topic

    def connect(self):
	    #manage connection to broker
        self._paho_mqtt.connect(self.broker , self.port) #arguments are hostname of the remote broker and network port of the server (1883)
        self._paho_mqtt.loop_start()    #network loop start  
    
    def subscribeToTopic(self, topic, QoS):
        # if needed, you can do some computation or error-check before subscribing
        print ("subscribing to '%s'" % (topic))

        if topic != self.topic:
            self._paho_mqtt.unsubscribe(self.topic)
            self.topic = topic  #register new topic if different from previous one
        
        # subscribe for a topic
        self._paho_mqtt.subscribe(topic, QoS) #arguments are topic and QoS
        
    def unsubscribe(self):
        self._paho_mqtt.unsubscribe(self.topic)
        
    def disconnect(self):
		# remember to unsuscribe if it is working also as subscriber 
        self._paho_mqtt.unsubscribe(self.topic)
        self._paho_mqtt.loop_stop()     #network loop stop        
        self._paho_mqtt.disconnect()    #disconnects from the broker cleanly
    
    def myOnConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to %s with result code: %d" % (self.broker, rc))

    def myOnMessageReceived (self, paho_mqtt , userdata, msg):
    	# A new message is received
        print("\t\tMessage received")
        self.notifier.notify (msg.topic, msg.payload)
    
#####################################################################    

