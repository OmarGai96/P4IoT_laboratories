##REST EXAMPLE 1

import random
import string
import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    #localhost:8080/
    #localhost:8080/index
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    #localhost:8080/generate
    #localhost:8080/generate?length=16
    def generate(self,length=8):
        return ''.join(random.sample(string.hexdigits,int(length)))
    
    @cherrypy.expose
    #localhost:8080/myMethod
    def myMethod(self):
        return "Provaaaa!"

    @cherrypy.expose
    #localhost:8080/display
    def display(self):
        cherrypy.session['mystring'] = "Ciao a tutti"
        return cherrypy.session['mystring']

if __name__=="__main__":
    conf = {
        '/': {'tools.sessions.on':True
              }
        }
    cherrypy.tree.mount(StringGenerator(),'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
