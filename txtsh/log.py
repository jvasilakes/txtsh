from __future__ import print_function

import traceback
import time
import subprocess


class Log(object):
    """
    A unified log manager.
    Implemented as a singleton to avoid
    nasty race-conditions.
    """

    _instance = None

    @classmethod
    def start(cls, filename):
        """
        If called when a log instance already exists,
        just return the existing log instance.
        """
        if not cls._instance:
            cls._instance = cls(filename)
        return cls._instance

    @classmethod
    def get(cls):
        """
        Get the existing log instance, creating
        one if necessary.
        """
        if cls._instance:
            return cls._instance
        else:
            cls._instance = cls()
            return cls._instance

    def __init__(self, filename):

        if self._instance:
            # This is a bit of a trick.
            # Since _instance must be a Log instance, use it to log our error.
            self._instance.write(mes="Tried to create more than one logger.")
            del self
            raise Exception("SingletonError: Tried to \
                            create more than one logger.")

        self.filename = filename
        self.timestamp = None

    def getTimestamp(self):
        return "[{0}]" .format(time.strftime("%H:%M:%S"))

    def getTracebackInfo(self):
        return traceback.format_exc()

    def write(self, mes=None, traceback=False):
        """
        Write message and or latest traceback to the logfile.
        One of message or traceback is required.
        """
        if not mes and not traceback:
            return

        if mes and type(mes) != str:
            mes = str(mes)

        with open(self.filename, 'a') as log:
            if traceback:
                tb = self.getTracebackInfo()
                line = "{0} ERROR \n{1} \n"
                info = [self.getTimestamp(), tb]
                log.write(line.format(*info))
                if mes:
                    log.write('\t "{}"' .format(mes))

            else:
                log.write("{0} {1} \n" .format(self.getTimestamp(), mes))

    def view(self):
        """
        View the logfile from within txtsh.
        """
        try:
            subprocess.call(['less', self.filename])
        except Exception as e:
            self.write(str(e), traceback=e)
            return

    def clear(self):
        open(self.filename, 'w').close()
        print("Logfile cleared.")


# Methods to facilitate use of the logger.
def start(filename):
    return Log.start(filename)


def write(mes=None, traceback=False):
    return Log.get().write(mes, traceback)


def view():
    return Log.get().view()


def clear():
    return Log.get().clear()


# Used for testing.
if __name__ == '__main__':
    l1 = Log.start('tst.log')
    try:
        1/0
    except:
        l1.write(traceback=True)
        print("Wrote traceback.")
