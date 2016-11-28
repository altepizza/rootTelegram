'''
Created on Nov, 27 2016

'''

import telepot
import ConfigParser
import socket
import getpass

config = ConfigParser.RawConfigParser()
config.read('config.ini')
telegramToken = config.get('Telegram', 'Token')
telegramChatID = config.getint('Telegram', 'ChatId')
bot = telepot.Bot(telegramToken)

def doSomething():
    text = "Login on " + socket.gethostname() + " by " + getpass.getuser()
    bot.sendMessage(telegramChatID, text)

if __name__ == '__main__':
    doSomething()
