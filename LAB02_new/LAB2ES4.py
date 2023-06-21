import cherrypy
import json

class myWebService:
    
    exposed = True
    def GET (self, *uri, **params):
        
        if len(uri) == 0:
            return open('./index.html','r').read()
        if len(uri) == 1:
            if uri[0] == "devicesList":
                devs = json.load(open("devices.json"))
                return json.dumps(devs, indent=4)
            else:    
                raise cherrypy.HTTPError(400, "Bad request")
                
        else:
           raise cherrypy.HTTPError(400, "Bad request")  
        
    def POST(self, *uri, **params):
        newDev = json.loads(cherrypy.request.body.read()) #read body to obtain description of a new device
        devices =  json.load(open("devices.json"))  #open the devices list from file
        devicesList = list(devices["devicesList"])  #obtain list of devices
        devicesList.append(newDev)                  #append new device in list
        devices["devicesList"] = devicesList        #update devices list
        json.dump(devices, open("devices.json", "w"), indent=4)    #update json file
        return json.dumps(devices, indent=4)        #return whole list of files
        

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
    
    