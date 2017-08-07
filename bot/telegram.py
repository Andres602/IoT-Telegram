import requests


class telegramBot:

    def __init__(self, token):
        self.url = "https://api.telegram.org/bot" + token + "/"

    def buildUrl(self, method, options=None):
        post = {
            'url': self.url + method,
            'json': options
        }
        return post

    def getUpdates(self, offset=False):
        post = None
        if(offset):
            post = self.buildUrl("getUpdates", {'offset': offset})
        else:
            post = self.buildUrl("getUpdates")
        r = requests.post(post['url'], json=post['json'])
        return r.json()

    def sendMessage(self, id, text, replymarkup=False):
        message = {"chat_id": id, "text": text, "parse_mode": "Markdown"}
        if(replymarkup):
            message['reply_markup'] = replymarkup
        post = self.buildUrl("sendMessage", message)
        r = requests.post(post['url'], json=post['json'])
        return r.json()

    def replyTo(self, m, text):
        message = {
            "chat_id": m['chat']['id'],
            "text": text,
            "parse_mode": "Markdown",
            "reply_to_message_id": m['message_id']
        }
        post = self.buildUrl('sendMessage', message)
        r = requests.post(post['url'], json=post['json'])
        return r.json()

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
        r = requests.post(post['url'], json=post['json'])
        return r.json()

    def ansCBQuery(self, id, text, alert=False):
        message = {
            "callback_query_id ": id,
            "text": text,
            "parse_mode": "Markdown"
        }
        if(alert):
            message['show_alert'] = alert
        post = self.buildUrl('answerCallbackQuery', message)
        r = requests.post(post['url'], json=post['json'])
        return r.json()


def main():
    #mybot = telegramBot("")
    #updates = mybot.getUpdates()
    # mybot.send_message(,"<b>hola</b>")
    # print(updates)

if __name__ == "__main__":
    main()
