from User import *
from House import *
import json

class Project():
    
    def __init__(self,name):
        self.projectName = name
        self.projectOwner = ""
        self.projectLastUpdate = ""
        self.userList = []
        self.houseList = []
        
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
        lista = []
        for u in self.userList:
            lista.append(u.getUser())
        return lista 
    
    def getHouseList(self):
        lista = []
        for h in self.houseList:
            lista.append(h.getHouse())
        return lista
        
    ## ADD methods for list
    
    def addUserToList(self, user):
        self.userList.append(user) 
           
    def addHouseToList(self,house):
        self.houseList.append(house)
    
    ## ADD NEW methods (when input value come from user)
    
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
        """userList received as a vector of dictionaries"""
        for u in userList:
            newUser = User()
            newUser.setName(u["userName"])
            newUser.setUserID(u["userID"])
            newUser.setChatID(u["chatID"])
            for h in u["houses"]:
                newUser.addHouse(h["houseID"])
            self.addUserToList(newUser)
            name = newUser.getName()
            print(f"\tUser {name} added")
           
            #print("\tlist of houses")  
            #houses=newUser.printHouses()

        return
    
    def createHousesList(self,housesList):
        """create a list of houses for the current project, housesList received as a vector of dictionaries"""
        for h in housesList:
            newHouse = House()
            newHouse.setHouseID(h["houseID"])
            newHouse.setUserID(h["userID"])
            
            for d in h["devicesList"]:
                res = newHouse.addDevice(d)
                if res == 0:
                    name = newHouse.getHouseID()
                    print(f"\tHouse with ID {name} added correctly")
                    break
                
    
            self.addHouseToList(newHouse)
           
        return res

    def searchDeviceByID(self, deviceID):
        """Search device inside all houses, given the deviceID"""
        res = 0
        f = 0
        for h in self.houseList:
            res = h.searchDevice(deviceID)
            if res == 1:
                break
        if res == 0:
            print(f"Device devID: {deviceID} not found")
            
        return res
        
    def searchDevicesByHouseID(self, houseID):
        """Search devices inside a given houseID"""
        hID = int(houseID)
        hFlag=0
        for h in self.houseList:
            if h.getHouseID() == hID:
                hFlag = 1
                print(f"Devices in house {hID}")
                h.printAllDevices()
                
        if hFlag == 0:
            print(f"House hID: {hID} not found")
            
        return hFlag
        
    def searchUserByUserID(self,userID):
        """Search user given the user ID"""
        uID = int(userID)
        uFlag=0
        for u in self.userList:
            if u.getUserID() == uID:
                uFlag = 1
                print(f"Info for user uID: {uID}")
                u.printAllInfo()
        if uFlag == 0:
            print(f"User uID: {uID} not found")
            
        return uFlag
            
    def searchDevicesByMeasureType(self, type):
        """Search all the device with the given measure type"""
        res = 0
        for h in self.houseList:
            res += h.searchTypeInDevices(type)
            
        if res == 0:
            print(f"No devices has measure type {type}")
        return res
    
    def insertDevice(self):
        """Insert a new device if it doesn't exist, modify otherwise"""
        devID = input("Write the device ID: ")
        hID = int(input("Write the house ID: "))
        uID = int(input("Write the user ID: "))
        
        if self.searchDeviceByID(devID) == 1:
            #device already exists
            for h in self.houseList:
                if hID == h.getHouseID():
                    h.modifyDeviceByID(devID)
        else:
            for h in self.houseList:
                if hID == h.getHouseID():
                    h.addNewDevice(devID)
                    
    def createProject(self, dictionary):
        """information of Project passed through a dictionary"""
        self.setProjectName(dictionary["projectName"])
        self.setOwner(dictionary["projectOwner"])
        self.setLastUpdate(dictionary["lastUpdate"])
        self.createUsersList(dictionary["usersList"])
        self.createHousesList(dictionary["houses"])
        return 1
    
    def save(self, fileName):
        myDictionary = {}
        myDictionary["projectName"] = self.projectName
        myDictionary["projectOwner"] = self.projectOwner
        myDictionary["lastUpdate"] = self.projectLastUpdate
        myDictionary["usersList"] = self.getUserList()
        myDictionary["houses"] = self.getHouseList()
        json.dump(myDictionary,open(fileName,"w"), indent=4)
        return 1
        