#!/usr/bin/python
# -*- coding: utf-8 -*-
from database import database
from telegramCurl import telegramBot
import json
import ast
from ConfigParser import SafeConfigParser
import requests.packages.urllib3
import time

config = SafeConfigParser()
config.read('/home/orangepi/IoT-Telegram/bot/config.ini')


def keyboard(status=None):
    on = 'ON    ⚪'
    off = 'OFF  ⚪'
    if(status == True):
        on = 'ON    🔵'
    if(status == False):
        off = 'OFF  🔵'
    keys = [[{'text': on, 'callback_data': '{"value":True}'}],
            [{'text': off, 'callback_data': '{"value":False}'}]]
    return json.dumps({'inline_keyboard': keys})


def turnOn(db,id):
    print ("turnOn")
    return db.turnOn(id)



def turnOff(db,id):
    print("turnOff")
    return db.turnOff(id)


def main():
    updateId = False
    requests.packages.urllib3.disable_warnings()
    bot = telegramBot(config.get('bot', 'token'))
    db=database(config.get('database','host'), config.get('database','port'))
    db.connect()
    print("Bot iniciado")
    while (1):
        updates = bot.getUpdates(updateId)
        if(len(updates['result'])):
            updates = updates['result']
            updates.sort(key=lambda x: x["update_id"], reverse=False)
            updateId = updates[-1]['update_id'] + 1
            for update in updates:
                if('message' in update):
                    id = update['message']['chat']['id']
                    if(update['message']['text'] == '/start'):
                        teclado = keyboard()
                        bot.sendMessage(
                            id, "Bienvenido al *IoT_Osite_0.0*", teclado)
                if('callback_query' in update):
                    id = update['callback_query']['message']['chat']['id']
                    msg_id = update['callback_query'][
                        'message']['message_id']
                    data = ast.literal_eval(
                        update['callback_query']['data'])
                    if(data['value']):
                        turnOn(db,id)
                    else:
                        turnOff(db,id)
                    teclado = keyboard(data['value'])
                    bot.editMessage(
                        id, msg_id, "Welcome to *IoT_Osite_1.0*", teclado)
        time.sleep(1)

    

if __name__ == "__main__":
    main()
