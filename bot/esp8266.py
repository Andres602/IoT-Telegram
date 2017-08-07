import requests


class light:

    def __init__(self, host):
        self.host = host

    def turnOn(self):
        requests.get(self.host + "/gpio/1")

    def turnOff(self):
        requests.get(self.host + "/gpio/0")
