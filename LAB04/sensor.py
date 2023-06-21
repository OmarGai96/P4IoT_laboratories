
import random
import json
import time

class Sensor():
	"""docstring for Sensor"""
	def __init__(self,buildingID,floorID,roomID,sensorID):
		self.buildingID=buildingID
		self.floorID=str(floorID)
		self.roomID=str(roomID)
		self.sensorID=str(sensorID)
		self.topic='/'.join([self.buildingID,self.floorID,self.roomID,self.sensorID])
		self.__message={
			'buildingID':self.buildingID,
			'floorID':self.floorID,
			'roomID':self.roomID,
			'bn':self.sensorID,
			'e':
				[
					{'n':'temperature','value':'', 'timestamp':'','unit':'C'},
					{'n':'humidity','value':'', 'timestamp':'','unit':'%'}
					]
			}
  
	def getSensorTopic(self):
		return self.topic

	def sendData(self):
		identifier = self.getSensorTopic()
		completeMessage = {}
		message=self.__message
		message['e'][0]['value']=random.randint(10,30) #Temp value
		message['e'][1]['value']=random.randint(50,90) #Hum value
		message['e'][0]['timestamp']=str(time.time()) #Time 
		message['e'][1]['timestamp']=str(time.time()) #Time 
		completeMessage["sensorID"] = identifier
		completeMessage["message"] = message
		json.dump(completeMessage,open("sensorValues.json", "w"),indent=4)
		print("Message send")

if __name__ == '__main__':
	conf=json.load(open("settings.json"))
	Sensors=[]  ##list of sensors
	buildingID=conf["baseTopic"]
	floorID=1 
	roomID=2 
	s=3
 
	#create only one sensor
	sensor=Sensor(buildingID,floorID,roomID,s) 
	Sensors.append(sensor)   

	while True:
		for sensor in Sensors:
			sensor.sendData() #saves fake data to a file (to exchange with myWebService)
			time.sleep(20)    #every 20 seconds
	
