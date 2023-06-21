from User import *
from House import *
import json
import time

class Project():
    
    def __init__(self,name):
        self.projectName = name
        self.projectOwner = ""
        self.projectLastUpdate = ""
        self.userList = []  #userList is a list of USER objects
        self.houseList = [] #houseList is a list of HOUSE objects
        
    #getter and setter methods
        
    def setOwner(self,name):
        self.projectOwner = name
        
    def getOwner(self):
        return str(self.projectOwner)
        
    def setProjectName(self,name):
        self.projectName = name
    
    def getProjectName(self):
        return str(self.projectName)
    
    def setLastUpdate(self,date):
        self.projectLastUpdate = date
        
    def getUserList(self):
        return self.userList
    
    def getHouseList(self):
        return self.houseList
        
    ## ADD methods for list
    
    def addUserToList(self, user):
        """append an USER obj to the list of users"""
        self.userList.append(user) 
           
    def addHouseToList(self,house):
        """append an HOUSE obj to the list of houses """
        self.houseList.append(house) 
    
    ## PRINT methods, to print info
     
    def printAll(self):
        """Print all the information of the current project"""
        print(f"Project owner: {self.projectOwner}")
        print(f"Project name: {self.projectName}")
        print(f"Project owner: {self.projectLastUpdate}")
        print("Users list:")
        for u in self.userList:
            u.printAllInfo()
        print("Houses list:")
        for h in self.houseList:
            h.printAllInfo()
        return    
    
    ## other methods    
    def createUsersList(self,userList):
        """create a list of users for the current project, userList received as a vector of dictionaries"""
        for u in userList:
            newUser = User()
            newUser.setName(u["userName"])
            newUser.setUserID(u["userID"])
            newUser.setChatID(u["chatID"])
            for h in u["houses"]:
                newUser.addHouse(h["houseID"]) #add houses to user, as a list of integers (the IDs)
            self.addUserToList(newUser)     ##add the user just created
            name = newUser.getName()
            print(f"\tUser {name} added")
        return 0
    
    def createHousesList(self,housesList):
        """create a list of houses for the current project, housesList received as a vector of dictionaries"""
        for h in housesList:
            newHouse = House()
            newHouse.setHouseID(h["houseID"])
            newHouse.setUserID(h["userID"])
            
            for d in h["devicesList"]:
                if newHouse.addDevice(d) == 0:  ##
                    hID = newHouse.getHouseID()
                    print(f"\tDevice added correctly in House with ID {hID} ")
                else:
                    print("Error adding device in house, aborted operation")
                
            self.addHouseToList(newHouse)
           
        return 0

    def searchDevice(self, deviceID):
        """Search device inside all houses, given the deviceID. Returns the houseID if success, -1 otherwise"""
        for h in self.houseList:
            if h.searchDevice(deviceID) != -1:
                return h.getHouseID()
        return -1
    
    def searchDeviceByID(self, deviceID):
        """Search device inside all houses, given the deviceID. Returns the device if success, -1 otherwise"""
        for h in self.houseList:
            dev = h.searchDevice(deviceID)
            if dev != -1:
                return dev
        return -1
        
    def searchDevicesByHouseID(self, houseID):
        """Search devices inside a given houseID. Returns the list of devices if success, -1 otherwise"""
        hID = int(houseID)
        for h in self.houseList:
            if h.getHouseID() == hID:
                return h.getAllDevices()      
        return -1
    
    def printDevicesByHouseID(self, houseID):
        """Search devices inside a given houseID and print. Returns 0 if success, -1 otherwise"""
        hID = int(houseID)
        for h in self.houseList:
            if h.getHouseID() == hID:
                h.printAllDevices()
                return 0     
        return -1
    
    def searchUserByUserID(self,userID):
        """Search user given the user ID. Returns the user if success, -1 otherwise"""
        uID = int(userID)
        for u in self.userList:
            if u.getUserID() == uID:
                return u.getUser()            
        return -1
    
    def printUserByUserID(self,userID):
        """Search user given the user ID. Returns 0 if success, -1 otherwise"""
        uID = int(userID)
        for u in self.userList:
            if u.getUserID() == uID:
                u.printAllInfo()
                return 0           
        return -1
            
    def searchDevicesByMeasureType(self, type):
        """Search all the device with the given measure type. Returns the list of devices if succes, -1 otherwise"""
        lista = []
        for h in self.houseList:
            res = 0
            res = h.searchTypeInDevices(type)
            if res != -1:            
                lista.append(res)
        if len(lista) != 0:
            return lista
        else: 
            return -1
        
    def printDevicesByMeasureType(self, type):
        """Search all the device with the given measure type. Returns 0 if success, -1 otherwise"""
        res = 0
        for h in self.houseList:
            if h.searchTypeInDevicesAndPrint(type) == 0:
                res += 1 
        if res != 0:
            return 0
        else: 
            return -1
    
    def insertDeviceManually(self): #old version is insertDevice
        """Insert a new device if it doesn't exist, modify otherwise. Returns 0 if success, -1 otherwise"""
        devID = input("Write the device ID: ")
        hID = int(input("Write the house ID: "))
        uID = int(input("Write the user ID: "))
        
        if self.searchDevice(devID) != -1:
            #device already exists
            for h in self.houseList:
                if hID == h.getHouseID():
                    if h.modifyDeviceByID(devID) == 0:
                        print("\tdevice modified successfully")
                        return 0
                    else:
                        return -1
        else:
            #device is new
            for h in self.houseList:
                if hID == h.getHouseID():
                    h.addNewDevice(devID) #check of return value is not needed
                    return 0 
            print("\tdevice cannot be added because house doesn't exist")
            return -1
                    
    def insertDevice(self, device, userID, houseID):
        """Insert a new device if it doesn't exist, modify otherwise"""
        
        hID = self.searchDevice(device["deviceID"])
        ## check presence of device
        if hID != -1 and hID == houseID:
            #device already exists
            for h in self.houseList:
                if hID == h.getHouseID():
                    if h.modifyDevice_REST(device) == 0:
                        self.save("newFile.json") #automatically save if success
                        return 0
                    else: 
                        return -1

        else:
            #new device
            for h in self.houseList:
                if houseID == h.getHouseID() and userID == h.getUserID():
                    if h.addNewDevice_REST(device) == 0:
                        self.save("newFile.json") #automatically save if success
                        return 0
                    else: 
                        return -1
                
        return -1
                    
    def getEmptyDevice(self):
        """Returns a device with empty fields"""
        dev = Device(-1, "")
        return dev.getDevice()
                    
    def createProject(self, dictionary):
        """information of Project passed through a dictionary. Returns 0 if success"""
        self.setProjectName(dictionary["projectName"])
        self.setOwner(dictionary["projectOwner"])
        self.setLastUpdate(dictionary["lastUpdate"])
        self.createUsersList(dictionary["usersList"])
        self.createHousesList(dictionary["houses"])
        return 0
    
    def save(self, fileName):
        myDictionary = {}
        myDictionary["projectName"] = self.projectName
        myDictionary["projectOwner"] = self.projectOwner
        today = str(datetime.today()) 
        myDictionary["lastUpdate"] =  today[0:10] + " " + today[11:16] #an example 2023-05-11:12:46:00
        myDictionary["usersList"] = self.getAllUsers()
        myDictionary["houses"] = self.getAllHouses()
        json.dump(myDictionary,open(fileName,"w"), indent=4)
        return 0
    
    def printDeviceByID(self, deviceID):
        """Search device inside all houses, given the deviceID. Returns the houseID if success, -1 otherwise"""
        for h in self.houseList:
            if h.searchDeviceAndPrint(deviceID) == 0:
                return 0
        return -1         
    
    def getAllUsers(self):
        listaToReturn = []
        for u in self.userList:
            listaToReturn.append(u.getUser())
        return listaToReturn
    
    def getAllHouses(self):
        listaToReturn = []
        for h in self.houseList:
            listaToReturn.append(h.getHouse())
        return listaToReturn 
    
    def exportAll(self):
        myDictionary = {}
        myDictionary["projectName"] = self.projectName
        myDictionary["projectOwner"] = self.projectOwner
        today = str(datetime.today()) 
        myDictionary["lastUpdate"] =  today[0:10] + " " + today[11:16] #an example 2023-05-11:12:46:00
        myDictionary["usersList"] = self.getAllUsers()
        myDictionary["houses"] = self.getAllHouses()
        return myDictionary