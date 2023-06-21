##REST EXAMPLE 2

import random
import string
import cherrypy

class StringGeneratorWebService(object):
    exposed = True

    def GET(self,*path,**query):
        #URI can be managed as a String
        return ("uri: %s; urilength: %s" %(str(path),len(path)))

    def POST(self,*path,**query):
        some_string = ''.join(random.sample(string.hexdigits,int(query['length'])))
        cherrypy.session['mystring'] = some_string
        return some_string

    def PUT(self,*path,**query):
        cherrypy.session['mystring']=params['another_string']

    def DELETE(self,*path,**query):
        cherrypy.session.pop('mystring', None)

if __name__=="__main__":
    conf = {
        '/': {
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
              }
        }
    cherrypy.tree.mount(StringGeneratorWebService(),'/string',conf)

    cherrypy.config.update({'server.socket_host':'0.0.0.0'})
    cherrypy.config.update({'server.socket_port':8080})
    
    cherrypy.engine.start()
    cherrypy.engine.block()    
