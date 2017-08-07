# -*- coding: utf-8 -*-
from database import database
from telegram import telegramBot
from esp8266 import light
import json
import ast
from ConfigParser import SafeConfigParser
import requests.packages.urllib3

config = SafeConfigParser()
config.read('config.ini')


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


def turnOn(esp):
    esp.turnOn()
    print ("turnOn")


def turnOff(esp):
    esp.turnOff()
    print ("turnOff")


def main():
    requests.packages.urllib3.disable_warnings()
    bot = telegramBot(config.get('bot', 'token'))
    esp = light(config.get('esp8266', 'host'))
    db = database(config.get('database', 'host'),
                  config.get('database', 'port'))
    db.connect()
    if(db.status()):
        print("Bot iniciado")
        while (1):
            updateId = db.getUpdate()
            updates = bot.getUpdates(updateId)
            if(len(updates['result'])):
                updates = updates['result']
                updates.sort(key=lambda x: x["update_id"], reverse=False)
                db.setUpdate(updates[-1]['update_id'] + 1)
                for update in updates:
                    if('message' in update):
                        id = update['message']['chat']['id']
                        if(update['message']['text'] == '/start'):
                            if(db.getLight(id) == None):
                                db.newUser(id)
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
                            turnOn(esp)
                        else:
                            turnOff(esp)
                        teclado = keyboard(data['value'])
                        bot.editMessage(
                            id, msg_id, "Bienvenido al *IoT_Osite_0.0*", teclado)

    else:
        print("Error al conectar a la base de datos")
        return 0


if __name__ == "__main__":
    main()
