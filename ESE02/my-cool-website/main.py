import cherrypy
import os


class Example():
    """docstring for Reverser"""
    exposed = True

    def __init__(self):
        self.id = 1

    def GET(self):
        return open("index.html")  ##open a file


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './css'
        },
        '/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './js'
        },
    }
    cherrypy.tree.mount(Example(), '/', conf) ##first param is the name of the class
    cherrypy.engine.start()
    cherrypy.engine.block()
