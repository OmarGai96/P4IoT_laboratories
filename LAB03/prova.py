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
        
    dict = project.searchDeviceByID(6)
    print("Device: ")
    print(dict)
    
    dict = project.searchUserByUserID(1)
    print("User: ")
    print(dict)