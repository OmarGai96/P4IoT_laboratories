##subclass 3 Device 

class Device:
    def __init__(self, ID, name):
        self.deviceID = int(ID)
        self.deviceName = name
        self.measureTypeList = []
        self.availableServices = []
        self.servicesDetails=[] #list of dictionaries
        self.lastUpdate = ""
    
    #getter and setter methods

    def getDeviceID(self):
        return int(self.deviceID)

    def setDeviceID(self, ID):
        self.deviceID = int(ID)
        return

    def getDeviceName(self):
        return self.deviceName

    def setDeviceName(self, name):
        self.deviceName = name
        return

    def getLastUpdate(self):
        return self.lastUpdate

    def setLastUpdate(self, last):
        self.lastUpdate = last
        return
    
    def getMeasureTypeList(self):
        return self.measureTypeList

    def getAvailableServices(self):
        return self.availableServices

    
    ## ADD methods for list
    
    def addMeasureType(self, measures):
        """measures received as a list"""
        for m in measures:
            print(f"\t\t\tnew MeasureType added {m}")
            self.measureTypeList.append(m)
        
        return

    def addAvailableService(self, services):
        """services received as a list"""
        for service in services:
            print(f"\t\t\tnew service added {service}")
            self.availableServices.append(service)
        return
    
    def addServiceDetail(self, servDet):
        "servDet received as a list of dictionary"
        flag = 0
        for s in servDet:
            serviceType = s["serviceType"]
            #consistency check
            for avServ in self.availableServices:
                #find if the serviceDetail refers to an existing available service
                if avServ == serviceType:
                    flag = 1    #service found
                    self.servicesDetails.append(s) #correct        
        if flag == 0:
            print("Error, specified service is not available") 
            return -1
        else: 
            return 1               
    
    ## ADD NEW methods (when input value come from user)
    
    def addNewMeasureType(self):
        flag = 1
        print("\tInsert list of measure type, -1 to finish")
        while(flag):
            mt = input("\t")
            if mt == "-1":
                flag = 0
            else:
                self.measureTypeList.append(mt)
        return 1
    
    def addNewAvailableService(self):
        flag = 1
        print("\tInsert list of available services, -1 to finish")
        while(flag):
            mt = input("\t")
            if mt == "-1":
                flag = 0
                return 1
            else:
                self.availableServices.append(mt)
        return 1
    


    def addNewServicesDetails(self):
        for s in self.availableServices:
            diz = {} # a dedicated dictionary for each service
            t = 1
            topList=[]
            IP = input(f"\t\tFor service {s} insert the service IP: ")
            while (t):
                topic = input(f"\t\tFor service {s} insert the topic [nothing if not defined]: ")
                if topic == "":
                    t = 0
                else:
                   topList.append(topic) 

            if len(topList) == 0:
                diz ={"serviceType": s, "serviceIP": IP}
            else:
                diz ={"serviceType": s, "serviceIP": IP, "topic": topList}
                
            self.servicesDetails.append(diz) 
        return 1
    
    ## PRINT methods, to print info

    def printAvailableServices(self):
        for i in self.availableServices:
            print(f"\t{i}")
        return
    
    def printMeasureTypes(self):
        for i in self.measureTypeList:
            print(f"\t{i}")
        return
    

    def printAllInfo(self):
        print(f"\t\tdeviceID: {self.deviceID}")
        print(f"\t\tdeviceName: {self.deviceName}")
        print(f"\t\tmeasure types: ", end='')
        for m in self.measureTypeList:
            print(f"{m} ", end='')
        print("\n\t\tAvailable Services: ", end='')
        for s in self.availableServices:
            print(f"{s} ", end='')
        print("\n\t\tServices details: ")
        for s in self.servicesDetails:
            diz=s.items()
            for d in diz:
                print(f"\t\t\t{d}")
        print(f"\t\tlast update: {self.lastUpdate}\n")
        return

    def printParameters(self):
        print("\tdeviceID")
        print("\tdeviceName")
        print("\tmeasureType")
        print("\tavailableServices")
        print("\tserviceDetails")
        return
    
    #OTHERS  methods

    def modifyParam(self, toModify):
        if toModify == "deviceID":
            print("new Device ID")
        elif toModify == "deviceName":
            print("new Device name")
        elif toModify == "measureType":
            print("new measure Type")
        elif toModify == "availableServices":
            print("new service")
        elif toModify == "serviceDetails":
            print("new detail")
        else:
            print("Error, no supported parameter")
        return
    
    def getDevice(self):
        dev = {}
        dev["deviceID"] = self.deviceID
        dev["deviceName"] = self.deviceName
        dev["measureType"] = self.measureTypeList
        dev["availableServices"] = self.availableServices
        dev["servicesDetails"] = self.servicesDetails
        dev["lastUpdate"] = self.lastUpdate
        return dev
        
