###MAIN CLASS
import cherrypy
import json

class myWebService:
    
    exposed = True

    def __init__(self):
        pass
    
    def GET(self,*uri):  
        if len(uri) == 0:
            return open('./index.html','r').read()
        else:
            if uri[0] == "devicesList":
                devices= json.loads(open('./devices.json','r').read())
                return json.dumps(devices, indent=4)
        
    def POST(self,*uri):
        myDict = json.loads(cherrypy.request.body.read())      #read the form received
        myDevs = json.loads(open('./devices.json','r').read()) #read existing file
        #f.close()
        listDevices = myDevs['devicesList']
        listDevices.append(myDict)
        myDevs['devicesList'] = listDevices

        f=open("./devicesNew.json",'w')
        json.dump(myDevs,f)
        f.close()
        return json.dumps(myDevs)

class mySecondWebService:

    exposed = True
    
    def GET(self,*uri,**query):
        return open('./devices.json','r').read()

#additional class useful if you want to ripristinate the previous version of 'devices.json' file
class flushClass:   

    exposed = True
    
    def GET(self,*uri,**query):     
        myDevs = json.loads(open('./devices.json','r').read()) #read existing file
        listDevices = myDevs['devicesList']
        listDevices.pop()
        myDevs['devicesList'] = listDevices
        f=open("devices.json",'w')
        json.dump(myDevs,f)
        f.close()
        return "done"

if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    cherrypy.tree.mount(myWebService(), '/', conf)
    cherrypy.tree.mount(flushClass(), '/flush', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()

    

    
