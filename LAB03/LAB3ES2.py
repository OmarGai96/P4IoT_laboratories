import json
import cherrypy
from Project import *

class myWebService:
    
    def __init__(self):
        print("Catalog\n")
        myDict = dict
        
        #open catalog from file and saves content into a dictionary
        fileCatalog = open("catalog.json","r")
        myDict = json.load(fileCatalog) 
        fileCatalog.close()
    
        #create a new project
        self.project = Project("newProject") 
        if self.project.createProject(myDict) == 0:
            print("Project successfully created")
    
    exposed = True
    
    def GET(self,*uri,**params):
        
        errorMessage={}
           
        if len(uri) == 0:
            return open("instructions.html", "r") 
         
        elif len(uri) == 1: 
            if uri[0] == '1':
                dev = self.project.searchDeviceByID(params["deviceID"])  #http://localhost:8080/1?deviceID=n
                if dev != -1:
                    return json.dumps(dev,indent=4)
                else:
                    errorMessage["Error"]="Device cannot be found"
                    return json.dumps(errorMessage,indent=4)
                
            elif uri[0] == '2':   
                devicesInHouse = self.project.searchDevicesByHouseID(params["houseID"]) #http://localhost:8080/2?houseID=n
                if devicesInHouse != -1:
                    return json.dumps(devicesInHouse)
                else:
                    errorMessage["Error"]="Device cannot be found in any house"
                    return json.dumps(errorMessage,indent=4)
            
            elif uri[0] == '3':
                user = self.project.searchUserByUserID(params["userID"]) #http://localhost:8080/3?userID=n
                if user != -1:
                    return json.dumps(user) 
                else:
                    errorMessage["Error"]="User cannot be found"
                    return json.dumps(errorMessage,indent=4)    
            
            elif uri[0] == '4':  
                devices = self.project.searchDevicesByMeasureType(params["type"]) #http://localhost:8080/4?type=n
                if devices != -1:
                    return json.dumps(devices)
                else:
                    errorMessage["Error"]="Device cannot be found with specified measure type"
                    return json.dumps(errorMessage,indent=4)
                
            elif uri[0] == '5':  
                dev = {}
                dev["userID"] = -1
                dev["houseID"] = -1
                dev["device"] = self.project.getEmptyDevice()
                return json.dumps(dev)
            
            elif uri[0] == '6':  
                catalog = self.project.exportAll()
                return json.dumps(catalog, indent=4)
                  
            else: 
                errorMessage["Error"]="Error: bad option selected, please try again" 
                return json.dumps(errorMessage,indent=4)
             
            
    def POST(self, *uri, **params):
        result={}
        if uri[0] == '5':
            newDevice = json.loads(cherrypy.request.body.read()) 
            userID = newDevice["userID"]
            houseID = newDevice["houseID"]
            if self.project.insertDevice(newDevice["device"], userID, houseID) == 0:
                result["Operation result"]="Success" 
                return json.dumps(result,indent=4)
            else:
                result["Operation result"]="Fail" 
                return json.dumps(result,indent=4)    
    
if __name__=="__main__":

    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on':True
        }
    }
    
    cherrypy.tree.mount(myWebService(),'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()

    
    
    