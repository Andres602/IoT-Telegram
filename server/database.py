import redis


class database:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        self.r = redis.StrictRedis(host=self.host, port=self.port, db=0)

    def newUser(self, id):
        return self.r.hset('user:' + str(id), "light:01", "off")

    def getLight(self, id):
        return self.r.hget('user:' + str(id), "light:01")

    def getAll(self, id):
        return self.r.hgetall('user:' + str(id))

    def turnOn(self, id):
        return self.r.hset('user:' + str(id), "light:01", "on")

    def turnOff(self, id):
        return self.r.hset('user:' + str(id), "light:01", "off")

    def getUpdate(self):
        return self.r.hget('bot:lightControl', "updateId")

    def setUpdate(self, id):
        return self.r.hset('bot:lightControl', "updateId", id)

    def status(self):
        try:
            a = self.r.ping()
            if(a):
                return True
            return False
        except:
            return False


def main():
    print("main")

if __name__ == "__main__":
    main()
