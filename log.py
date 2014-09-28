import time
import subprocess


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

        self.timestamp = None

    def getTimestamp(self):

        self.timestamp = '[' + time.strftime("%H:%M:%S") + '] '

    def write(self, string):

        self.getTimestamp()

        with open(self.filename, 'a') as log:
            log.write(self.timestamp + string + '\n')

    def view(self):

        try:
            subprocess.call(['less', self.filename])
        except Exception as e:
            print e
            return


def write(string):
    return Log.get().write(string)
