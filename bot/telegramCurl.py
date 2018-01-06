# -*- coding: utf-8 -*-
import pycurl
import json
from StringIO import StringIO
from urllib import urlencode


class telegramBot:

    def __init__(self, token):
        self.url = "https://api.telegram.org/bot" + token + "/"
        self.c = pycurl.Curl()

    def close(self):
        self.c.close()

    def buildUrl(self, method, options=None):
        storage = StringIO()
        self.c.setopt(self.c.URL,  self.url + method)
        if(options != None):
            postfields = urlencode(options)
            self.c.setopt(self.c.POSTFIELDS, postfields)
        self.c.setopt(self.c.WRITEFUNCTION, storage.write)
        self.c.perform()
        content = storage.getvalue()
        return json.loads(content)

    def getUpdates(self, offset=False):
        post = None
        if(offset):
            post = self.buildUrl("getUpdates", {'offset': offset})
        else:
            post = self.buildUrl("getUpdates")
        return post

    def sendMessage(self, id, text, replymarkup=False):
        message = {"chat_id": id, "text": text, "parse_mode": "Markdown"}
        if(replymarkup):
            message['reply_markup'] = replymarkup
        post = self.buildUrl("sendMessage", message)
        return post

    def replyTo(self, m, text):
        message = {
            "chat_id": m['chat']['id'],
            "text": text,
            "parse_mode": "Markdown",
            "reply_to_message_id": m['message_id']
        }
        post = self.buildUrl('sendMessage', message)
        return post

    def editMessage(self, id, msg_id, text, replymarkup=False):
        message = {
            "chat_id": id,
            "message_id": msg_id,
            "text": text,
            "parse_mode": "Markdown"
        }
        if(replymarkup):
            message['reply_markup'] = replymarkup
        post = self.buildUrl('editMessageText', message)
        return post

    def ansCBQuery(self, id, text, alert=False):
        message = {
            "callback_query_id ": id,
            "text": text,
            "parse_mode": "Markdown"
        }
        if(alert):
            message['show_alert'] = alert
        post = self.buildUrl('answerCallbackQuery', message)
        return post


def main():
    bot = telegramBot('306060926:AAFYOStDUfL1PQ2wtvV16isS-ER8tDr8BHE')
    bot.getUpdates()
    bot.sendMessage(5951788, "hola _Mundo_")
    bot.close()

if __name__ == "__main__":
    main()

