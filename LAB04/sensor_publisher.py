
import random
import json
import time
from myPublisher import *

class Sensor():
	"""docstring for Sensor"""
	def __init__(self,baseTopic,sensorID):
		self.clientID = "1234"
		self.publisher = MyPublisher(self.clientID,self)
		self.publisher.setup("settings.json")
		topic = self.publisher.getTopic()
		self.topic='/'.join([topic,sensorID])
		print(f"Starting topic {self.topic}")
		self.__message={ 
			'e':
				[
					{'n':'temperature','v':'', 't':'','u':'Cel'},
					{'n':'humidity','v':'', 't':'','u':'%'}
					]
			}
  
	def start(self):
		self.publisher.connect()
  
	def stop(self):
		self.publisher.disconnect()
  
	def getSensorTopic(self):
		return self.topic

	def sendData(self):
		identifier = self.getSensorTopic()
		topic1 = identifier+"/temperature"
		topic2 = identifier+"/humidity"
		topic3 = identifier+"/allSensor"
		completeMessage1 = {}
		completeMessage2 = {}
		completeMessage3 = {}
		message=self.__message #retrieve original message
		#Set values
		message['e'][0]['v']=random.randint(10,30) #Temp value
		message['e'][1]['v']=random.randint(50,90) #Hum value
		message['e'][0]['t']=str(time.time()) #Time 
		message['e'][1]['t']=str(time.time()) #Time 
		#Set info
		completeMessage1["bn"] = topic1
		completeMessage2["bn"] = topic2
		completeMessage3["bn"] = topic3
		pack = []
		pack.append(message['e'][0])
		pack.append(message['e'][1])
		completeMessage1['e'] = []
		completeMessage2['e'] = []
		completeMessage1['e'].append(pack[0])
		completeMessage2['e'].append(pack[1])
		completeMessage3['e'] = pack
		#Send data
		self.publisher.publish(topic1,completeMessage1,2)
		self.publisher.publish(topic2,completeMessage2,2)
		self.publisher.publish(topic3,completeMessage3,2)
		
		#json.dump(completeMessage,open("sensorValues.json", "w"),indent=4)
		print("Messages send")

if __name__ == '__main__':
	conf=json.load(open("settings.json"))
	Sensors=[]  ##list of sensors
	baseTopic=conf["baseTopic"]
	s="sensor1"
 
	#create only one sensor
	sensor=Sensor(baseTopic,s) 
	sensor.start()
	Sensors.append(sensor)
	

	while True:
		for sensor in Sensors:
			sensor.sendData() #send data via MQTT 
			time.sleep(10)    #every 10 seconds
	
