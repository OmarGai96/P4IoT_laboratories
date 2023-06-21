from Device import *
from datetime import datetime

class House:
    def __init__ (self):
        self.userID = -1
        self.houseID = -1
        self.deviceList = []  ##list of Devices

    #getter and setter methods
    
    def getUserID(self):
        return self.userID

    def setUserID(self, newID):
        self.userID = int(newID)
        return 

    def getHouseID(self):
        return self.houseID

    def setHouseID(self, newID):
        self.houseID = int(newID)
        return 

    def getDeviceList(self):
        "returns a list of Devices"
        return self.deviceList
    
    ## ADD methods for list
    
    def addDevice(self,newDev):
        deviceToAdd = Device(newDev["deviceID"], newDev["deviceName"])
        deviceToAdd.addMeasureType(newDev["measureType"])
        deviceToAdd.addAvailableService(newDev["availableServices"])
        deviceToAdd.setLastUpdate(newDev["lastUpdate"])
        res=deviceToAdd.addServiceDetail(newDev["servicesDetails"])
        self.deviceList.append(deviceToAdd)

        if res == 0:
            print(f"no error found for device {deviceToAdd.getDeviceName()}, continue")
            return 0
        else: 
            return 1

    ## ADD NEW methods (when input value come from user)
    
    def addNewDevice(self,devID):
        new = Device(devID,"")
        name=input("\tInsert name of your device: ")
        lista = []
        new.setDeviceName(name)
        new.addNewMeasureType()
        new.addNewAvailableService()
        new.addNewServicesDetails()
        
        today = str(datetime.today())
        print(f"Today is {today[0:10]}")
        new.setLastUpdate(today[0:10])
        self.deviceList.append(new)
        return 

    ## PRINT methods, to print info
            
    def printAllInfo(self):
        print(f"\tuserID: {self.userID}")
        print(f"\thouseID: {self.houseID}")
        print("\tList of devices in house:")
        for d in self.deviceList:
            d.printAllInfo()
            
    def printAllDevices(self):
        for d in self.deviceList:
            d.printAllInfo()
                    
    #OTHERS  methods
    
    def searchDevice(self,deviceID):
        dev = int(deviceID)
        f = 0
        for d in self.deviceList:
            if d.getDeviceID() == dev:
                d.printAllInfo()
                f = 1
        return f  

    def searchTypeInDevices(self, typeMT):
        res = 0
        for dev in self.deviceList:
            for m in dev.getMeasureTypeList():
                if typeMT == m:
                    print("\tMeasure type available")
                    dev.printAllInfo()
                    #print("\n")
                    res=1
        return res
  
    def modifyDeviceByID(self,devID):
        devID = int(devID)
        for d in self.deviceList:
            if d.getDeviceID() == devID:
                d.printAllInfo()
                print("PRINT ALL PARAMETERS of Device")
                d.printParameters()
                param = input("What parameter to modify? ")
                d.modifyParam(param)
                
                today = str(datetime.today())
                return 1
             #   new.update(today[0:10])
        return 0
    
    def getHouse(self):
        selfHouse = {}
        selfHouse["userID"] = self.userID
        selfHouse["houseID"] = self.houseID
        lista = []
        for d in self.deviceList:
            lista.append(d.getDevice())
        selfHouse["devicesList"] = lista
        return selfHouse

    
        
