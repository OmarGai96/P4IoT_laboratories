import json
from Project import *

if __name__=="__main__":
    print("Catalog\n")
    name = ""
    myDict = dict
    
    fileCatalog = open("catalog.json","r")
    myDict = json.load(fileCatalog)
    fileCatalog.close()
    
    project = Project("newProject")
    if project.createProject(myDict) == 1:
        print("Project successfully created")
    
    menu = 1
    change = 0
    
    while(menu):
        print("\n\n")
        print("Type the operation to perform: ")
        print("1) search a device by ID")
        print("2) search a device by house ID")
        print("3) search a user by ID")
        print("4) search devices by measure type")
        print("5) insert a new device")
        print("6) print all information of the catalog")
        print("7) exit")
        choice = int(input("Choose option: "))
        if choice == 1:
            devID = input("Print all info for the given device ID: ")
            project.searchDeviceByID(devID)  
              
        elif choice == 2:   
            houseID = input("Print all info about devices for the given house ID: ")
            project.searchDevicesByHouseID(houseID) 
        
        elif choice == 3:
            userID=input("Print all info for the given user ID: ")
            project.searchUserByUserID(userID)    
        
        elif choice == 4:  
            type=input("Find devices with measure type: ")
            project.searchDevicesByMeasureType(type)  
        
        elif choice == 5:  
            change = 1  
            project.insertDevice()
        
        elif choice == 6:  
            print("Now print all info\n")
            project.printAll() 
             
        elif choice == 7:
            if input("Do you want to save? [yes/no]: ")== "yes":
                if change == 1:
                    project.save("catalog.json")
                #project.save("catalog2.json")
            menu = 0    
        else: 
            print("Error: bad option selected, please try again")


    #TODO: if a new device is inserted but the houseID is not defined forr the given UserID, what to do? 
    




    

    
    
    