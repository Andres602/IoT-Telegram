import requests


class light:

    def __init__(self, host):
        self.host = host

    def turnOn(self):
        try:
            requests.get(self.host + "/gpio/1")
        except:
            pass

    def turnOff(self):
        try:
            requests.get(self.host + "/gpio/0")
        except:
            pass
