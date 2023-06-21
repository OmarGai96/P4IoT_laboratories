import json
import requests
    
def insertDevice(device):
    """Fill the field of a device and return device serialized as a string
    {
    "userID": -1,
    "houseID": -1,
    "device": {
        "deviceID": -1,
        "deviceName": "",
        "measureType": [],
        "availableServices": [],
        "servicesDetails": [],
        "lastUpdate": ""
        }
    }"""
    device = {}
    info = {}
    device["userID"] = int(input("Write the user ID: "))
    device["houseID"] = int(input("Write the house ID: "))
    info["deviceID"] = int(input("Write the device ID: "))
    info["deviceName"] = input("Write the device name: ")
    flag = 1
    print("\tInsert list of measure type, -1 to finish")
    lista = []
    while(flag):
        mt = input("\t")
        if mt == "-1":
            flag = 0
        else:
            lista.append(mt)
    info["measureType"] = lista
    
    print("\tInsert list of available services, -1 to finish")
    lista = []
    flag = 1
    while(flag):
        mt = input("\t")
        if mt == "-1":
            flag = 0
        else:
            lista.append(mt)
    info["availableServices"] = lista
    
    servicesDetails = []
    
    for s in lista:
        diz = {} # a dedicated dictionary for each service
        t = 1
        topList=[]
        IP = input(f"\t\tFor service {s} insert the service IP: ")
        while (t):
            topic = input(f"\t\tFor service {s} insert the topic [nothing if not defined or exit]: ")
            if topic == "":
                    t = 0
            else:
               topList.append(topic) 

        if len(topList) == 0:
            diz ={"serviceType": s, "serviceIP": IP}
        else:
            diz ={"serviceType": s, "serviceIP": IP, "topic": topList}
                
            servicesDetails.append(diz) 
    info["servicesDetails"] = servicesDetails
    
    info["lastUpdate"] = input("Write the last update: ")
    device["device"] = info
    return json.dumps(device)

if __name__=="__main__":
    
    print("Welcome")
    flag = True
    while(flag):
        print("List of available services")
        print("- 1. searchDeviceByID: print all the information about the device for the given deviceID")
        print("- 2. searchDevicesByHouseID: print all the information about the devices for the given houseID")
        print("- 3. searchUserByUserID: print all the information of a user given its userID")
        print("- 4. searchDevicesByMeasureType: print all the information about any device that provides such measure type")
        print("- 5. insertDevice: insert a new device it that is not already present on the list (the ID is checked) given the device details,") 
        print("     the user ID and the house ID.")
        print("     Otherwise, update the information about the existing device with the new parameters")
        print("- 6. printAll: print the full catalog")
        print("- 9. exit")
        
        choice = int(input("Choose option: "))
        if choice == 9:
            flag = False
            
        elif choice == 1:
            devID = input("\tPrint all info for the given device ID: ")
            req = "http://localhost:8080/1?deviceID="+str(devID)
            print(f"your request: {req}")
            r = requests.get(req) #make the request - GET
            print(json.dumps(r.json(),indent=4)) #print response from Server
            
        elif choice == 2:   
            houseID = input("Print all info about devices for the given house ID: ")
            req = "http://localhost:8080/2?houseID="+str(houseID)
            print(f"your request: {req}")
            r = requests.get(req) #make the request - GET
            print(json.dumps(r.json(),indent=4)) #print response from Server
        
        elif choice == 3:
            userID=input("Print all info for the given user ID: ")
            req = "http://localhost:8080/3?userID="+str(userID)
            print(f"your request: {req}") 
            r = requests.get(req) #make the request - GET
            print(json.dumps(r.json(),indent=4)) #print response from Server
            
        elif choice == 4:  
            type=input("Find devices with measure type: ")
            req = "http://localhost:8080/4?type="+str(type)
            print(f"your request: {req}")
            r = requests.get(req) #make the request - GET
            print(json.dumps(r.json(),indent=4))   #print response from Server
            
        elif choice == 5:  
            dev = {}
            req = "http://localhost:8080/5"
            print(f"your request: {req}") 
            r = requests.get(req) #make the request - GET
            print("Response from server indicates the fields to be filled in order to insert a new device")
            print(json.dumps(r.json(),indent=4)) #print response from Server
            dev = r.json()
            
            #print(insertDevice(dev))
            #dev = insertDevice(dev)
            
            dev = json.load(open("newDevice.json"))
            dev = json.dumps(dev, indent=4)
            
            r = requests.post(req, dev) #make the request - POST
            print(json.dumps(r.json(),indent=4)) #print response from Server
            
        elif choice == 6:  
            req = "http://localhost:8080/6"
            print(f"your request: {req}") 
            r = requests.get(req)   #make the request - GET
            print(json.dumps(r.json(),indent=4)) #print response from Server
                    
        else: 
            print("Error: bad option selected, please try again")
            
        """ ## How to request services
    print("\n\n")
    print("- 1. http://localhost:8080/1?deviceID=n    where n is the deviceID")
    print("- 2. http://localhost:8080/2?houseID=n     where n is the houseID")
    print("- 3. http://localhost:8080/3?userID=n      where n is the userID")
    print("- 4. http://localhost:8080/4?type=string   where string is the measureType")
    print("- 5. http://localhost:8080/5   ")
    print("- 6. http://localhost:8080/6 ") """
    
