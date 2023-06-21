import json
import cherrypy
import telepot
from telepot.loop import MessageLoop

class RESTbot:
    
    exposed = True
    
    def __init__(self, tokenbot):
        self.tokenbot = tokenbot
        self.bot = telepot.Bot(self.tokenbot)
        self.usersList = []
        self.numberOfUsers = 0
        MessageLoop(self.bot, {'chat': self.on_chat_message}).run_as_thread()
        
        print("Bot started")
    
    def on_chat_message(self, msg):
        content_type, chat_type, chat_ID = telepot.glance(msg)
        self.numberOfUsers +=1 
        newUser = {}
        message = msg['text']
        
        if message == "/start":
            self.bot.sendMessage(chat_ID, text=f"Welcome 🤗")  ## activate service when start
            newUser["userID"] = self.numberOfUsers 
            newUser["chatID"] = chat_ID
            self.usersList.append(newUser) #register the new user
        else: 
            self.bot.sendMessage(chat_ID, text="Bad request 🧐")
        
        
    def POST(self, *uri, **params):
        tosend=''
        output={"status":"not-sent","message":tosend}
        if len(uri)!=0:
            userID = uri[0] ##userID is (or can be) passed as uri[0]
            body=cherrypy.request.body.read()
            jsonBody=json.loads(body)
            alert=jsonBody["alert"]
            action=jsonBody["action"]
            tosend=f"ATTENTION!!!\n{alert}, you should {action}"
            output={"status":"sent","message":tosend}
            for u in self.usersList:
                if int(u["userID"]) == int(userID):
                    self.bot.sendMessage(u["chatID"], text=tosend) #send message to right user
        return json.dumps(output)
   
if __name__ == '__main__':
    t = json.load(open("../../Telegram/settings.json")) #load settings from file
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    cherrypy.tree.mount(RESTbot(t["token"]), '/', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()

    

    
