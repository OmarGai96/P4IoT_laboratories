import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import json
import requests
import time
from MyMQTT import *

########### SIMPLE ECHO BOT EXAMPLE ############################

class EchoBot:
    def __init__(self, token):
        # Local token
        self.tokenBot = token
        self.bot = telepot.Bot(self.tokenBot) #create an instance of class Bot
        
        MessageLoop(self.bot, {'chat': self.on_chat_message}).run_as_thread() #set on_chat_message callback function

    def on_chat_message(self, msg):
        """on_chat_message callback"""
        content_type, chat_type, chat_ID = telepot.glance(msg)
        message = msg['text'] #read message content

        self.bot.sendMessage(chat_ID, text="You sent:\n"+message) #reply
        self.bot.sendMessage(chat_ID, text="How are you? \n")   #another (optional) reply
########### SIMPLE ECHO BOT EXAMPLE END############################


########### SIMPLE SWITCH BOT EXAMPLE ############################

class SimpleSwitchBot:
    def __init__(self, token, broker, port, topic):
        # Local token
        self.tokenBot = token
              
        self.bot = telepot.Bot(self.tokenBot)
        self.client = MyMQTT("telegramBot", broker, port, None)
        self.client.start()
        self.topic = topic
        self.__message = {'bn': "telegramBot",
                          'e':
                          [
                              {'n': 'switch', 'v': '', 't': '', 'u': 'bool'},
                          ]
                          } #SenML message to sent through mqtt
        MessageLoop(self.bot, {'chat': self.on_chat_message}).run_as_thread()

    def on_chat_message(self, msg):
        content_type, chat_type, chat_ID = telepot.glance(msg)
        message = msg['text']
        if message == "/switchOn":
            payload = self.__message.copy()
            payload['e'][0]['v'] = "on"
            payload['e'][0]['t'] = time.time()
            self.client.myPublish(self.topic, payload)
            self.bot.sendMessage(chat_ID, text="Led switched on")
        elif message == "/switchOff":
            payload = self.__message.copy()
            payload['e'][0]['v'] = "off"
            payload['e'][0]['t'] = time.time()
            self.client.myPublish(self.topic, payload)
            self.bot.sendMessage(chat_ID, text="Led switched off")
        elif message == "/sayHello":
            self.bot.sendMessage(chat_ID, text="Hello")
        else:
            self.bot.sendMessage(chat_ID, text="Command not supported")
########### SIMPLE SWITCH BOT EXAMPLE  END ############################


########### SWITCH BOT EXAMPLE ############################
class SwitchBot:
    def __init__(self, token, broker, port, topic):
        # Local token
        self.tokenBot = token
        # Catalog token
        # self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot = telepot.Bot(self.tokenBot)
        self.client = MyMQTT("telegramBotOrlando", broker, port, None)
        self.client.start()
        self.topic = topic
        self.__message = {'bn': "telegramBot",
                          'e':
                          [
                              {'n': 'switch', 'v': '', 't': '', 'u': 'bool'},
                          ]
                          }
        MessageLoop(self.bot, {'chat': self.on_chat_message,
                               'callback_query': self.on_callback_query}).run_as_thread()

    def on_chat_message(self, msg):
        content_type, chat_type, chat_ID = telepot.glance(msg)
        message = msg['text']
        if message == "/switch":
            buttons = [[InlineKeyboardButton(text=f'ON 😬', callback_data=f'on'), 
                    InlineKeyboardButton(text=f'OFF 🥶', callback_data=f'off')]]
            keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
            self.bot.sendMessage(chat_ID, text='What do you want to do', reply_markup=keyboard)
        else:
            self.bot.sendMessage(chat_ID, text="Command not supported")

    def on_callback_query(self,msg):
        query_ID , chat_ID , query_data = telepot.glance(msg,flavor='callback_query')

        payload = self.__message.copy()
        payload['e'][0]['v'] = query_data
        payload['e'][0]['t'] = time.time()
        self.client.myPublish(self.topic, payload) #send message to led via MQTT
        self.bot.sendMessage(chat_ID, text=f"Led switched {query_data}") #reply with status
      
########### SWITCH BOT EXAMPLE END ############################


if __name__ == "__main__":
    conf = json.load(open("settings.json"))
    token = conf["token"]
    broker = conf["brokerIP"]
    port = conf["brokerPort"]
    topic = conf["mqttTopic"]

#important: only one bot instance can be active 

    # Echo bot
    #bot=EchoBot(token)

    # SimpleSwitchBot
    #ssb = SimpleSwitchBot(token, broker, port, topic)
    
    # SwitchBot
    sb=SwitchBot(token,broker,port,topic)
    

    print("Bot started ...")
    
    while True:
        time.sleep(3)
        pass
