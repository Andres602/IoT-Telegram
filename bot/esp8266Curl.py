import pycurl
import json
from StringIO import StringIO
from urllib import urlencode


class light:

    def __init__(self, host):
        self.c = pycurl.Curl()
        self.host = host

    def requests(self,url):
        try:
            storage = StringIO()
            self.c.setopt(self.c.URL,  self.host + url)
            self.c.setopt(self.c.WRITEFUNCTION, storage.write)
            self.c.perform()
        except:
            pass

    def turnOn(self):
        self.requests("/gpio/1")

    def turnOff(self):
        self.requests("/gpio/0")

    

