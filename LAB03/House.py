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
            return -1

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
        new.setLastUpdate(today[0:10])
        self.deviceList.append(new)
        return 0

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
        for d in self.deviceList:
            if d.getDeviceID() == dev:
                #d.printAllInfo()
                return d.getDevice()
        return -1 ##if device not found, get an error  
    
    def searchDeviceAndPrint(self,deviceID):
        """Print the information of device (if exists), given its deviceID. Returns 0 if success, -1 otherwise"""
        dev = int(deviceID)
        for d in self.deviceList:
            if d.getDeviceID() == dev:
                d.printAllInfo()
                return 0
        return -1 ##if device not found, get an error

    def searchTypeInDevices(self, typeMT):
        """Search all the devices in house with given measure type. Returns the list of devices if success, -1 otherwise"""
        res = 0
        deviceList = []
        for dev in self.deviceList:
            for m in dev.getMeasureTypeList():
                if typeMT == m:
                    deviceList.append(dev.getDevice())   
        if len(deviceList) != 0:
            return deviceList
        else:
            return -1

    def searchTypeInDevicesAndPrint(self, typeMT):
        """Search all the devices in house with given measure type. Returns 0 if success, -1 otherwise"""
        res = 0
        deviceList = []
        #retrieve all the devices with given measure type
        for dev in self.deviceList:
            for m in dev.getMeasureTypeList():
                if typeMT == m:
                    deviceList.append(dev)   
        
        if len(deviceList) != 0:
            #print all the devices found            
            for d in deviceList:
                d.printAllInfo()
            return 0
        else:
            return -1
  
    def modifyDeviceByID(self,devID):
        """Modify the device given its deviceID. Returns 0 if success, -1 otherwise"""
        devID = int(devID)
        for d in self.deviceList:
            #retrieve device with deviceID <devID>
            if d.getDeviceID() == devID: 
                d.printAllInfo()
                print("PRINT ALL PARAMETERS of Device")
                d.printParameters()
                param = input("What parameter to modify? ")
                d.modifyParam(param)
                today = str(datetime.today())
                d.update(today[0:10])
                return 0
        return -1  
    
    def getHouse(self):
        selfHouse = {}
        selfHouse["userID"] = self.userID
        selfHouse["houseID"] = self.houseID
        selfHouse["devicesList"] = self.getAllDevices()
        return selfHouse

    def getAllDevices(self):
        devList = [] 
        for d in self.deviceList:
            devList.append(d.getDevice())
        return devList
    
    #######
    
    def findInList(self, item, lista):
        """search if 'item' is present in 'lista', list of strings"""
        for i in lista:
            if i == item:
                return 0
        return -1
        
    def addNewDevice_REST(self,device):
        new = Device(-1,"")
        new.setDeviceID(device["deviceID"])
        new.setDeviceName(device["deviceName"])
        new.addMeasureType(device["measureType"])
        new.addAvailableService(device["availableServices"])
        if new.addServiceDetail(device["servicesDetails"]) == -1:
            print("Error: service is not available, aborted operation")
            return -1
        today = str(datetime.today())
        print(f"Today is {today[0:10]}")
        new.setLastUpdate(today[0:10])
        
        self.deviceList.append(new) #update current list of devices
        return 0
    
    def modifyDevice_REST(self,device):
        mod = 0
        index = -1
        for d in self.deviceList:
            index += 1
            if d.getDeviceID() == device["deviceID"]:
                # if device["deviceName"] != d.getDeviceName():
                #     d.setDeviceName(device["deviceName"])
                #     mod += 1
                # for m in device["measureType"]:
                #     if self.findInList(m,d.getMeasureTypeList()) == -1:  
                #         #in case a measure type is new, update list
                #         d.addMeasureType(m)
                #         mod += 1
                # lista = device["availableServices"]
                # for s in lista:
                #     if self.findInList(s,d.getAvailableServices()) == -1:
                #         #in case a service is new, update list
                #         d.addOneService(s)
                #         mod += 1

                # if d.addNewServicesDetails_REST(device) == -1:
                #     print("Error: aborted operation")
                # else:
                #     mod += 1
                self.deviceList.pop(index) #remove old device
                mod = 1
                d = Device(device["deviceID"],device["deviceName"])
                d.addMeasureType(device["measureType"])
                d.addAvailableService(device["availableServices"])
                d.addServiceDetail(device["servicesDetails"])
                self.deviceList.insert(index, d)
        if mod == 0:
            print("No modifications have been done")
            return -1
        else:
            print(f"{mod} modifications have been done")   
            today = str(datetime.today())
            d.setLastUpdate(today[0:10])
            today = str(datetime.today())
            return 0
 
