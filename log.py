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

        self.filename = ".txtsh_log"

        self.timestamp = None

    def getTimestamp(self):

         return "[{0}]" .format(time.strftime("%H:%M:%S"))

    def write(self, string, error=None):

        if type(string) != str:
            string = str(string)

        with open(self.filename, 'a') as log:
            if error:
                log.write("{0} ERROR: {1} \n" \
                          .format(self.getTimestamp(), \
                          string)
                         )
            else:
                log.write("{0} {1} \n" .format(self.getTimestamp(), string))

    def view(self):

        try:
            subprocess.call(['less', self.filename])
        except Exception as e:
            self.write(str(e))
            return

    def clear(self):
        
        open(self.filename, 'w').close()
        print "Logfile cleared."


def write(string, error=None):
    return Log.get().write(string, error)

def view():
    return Log.get().view()

def clear():
    return Log.get().clear()
