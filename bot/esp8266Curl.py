import pycurl
import json
from StringIO import StringIO
from urllib import urlencode


class light:

    def __init__(self, host):
        self.c = pycurl.Curl()
        self.host = host

    def turnOn(self):
        storage = StringIO()
        self.c.setopt(self.c.URL,  self.host + "/gpio/1")
        self.c.setopt(self.c.WRITEFUNCTION, storage.write)
        self.c.perform()
        #requests.get(self.host + "/gpio/1")

    def turnOff(self):
        storage = StringIO()
        self.c.setopt(self.c.URL,  self.host + "/gpio/0")
        self.c.setopt(self.c.WRITEFUNCTION, storage.write)
        self.c.perform()
        #requests.get(self.host + "/gpio/0")

