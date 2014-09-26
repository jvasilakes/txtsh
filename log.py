import time


class Log(object):

    _instance = None

    @classmethod
    def start(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def get(cls):
        if cls._instance:
            return cls._instance
        else:
            cls._instance = cls()
            return cls._instance

    def __init__(self):

        self.filename = ".log"

        self.timestamp = self.getTimestamp()

    def getTimestamp(self):

        self.timestamp = '[' + time.strftime("%H:%M:%S") + ']'

    def writeLog(self, string):

        self.getTimestamp()

        with open(self.filename, 'a') as log:
            log.write(self.timestamp + string + '\n')
