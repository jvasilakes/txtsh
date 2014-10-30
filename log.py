from __future__ import print_function

import sys
import traceback
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

    def getTracebackInfo(self):
        t, val, tb = sys.exc_info()
        lines = traceback.format_exc().splitlines()
        return lines[-1], tb.tb_lineno

    def write(self, mes=None, traceback=False):
        if not mes and not traceback:
            return

        if mes and type(mes) != str:
            mes = str(mes)

        with open(self.filename, 'a') as log:
            if traceback:
                tb, lineno = self.getTracebackInfo()
                line = "{0} ERROR line {1}: {2} \n"
                info = [self.getTimestamp(), lineno, tb]
                log.write(line.format(*info))
                if mes:
                    log.write('\t "{}"' .format(mes))

            else:
                log.write("{0} {1} \n" .format(self.getTimestamp(), mes))

    def view(self):
        try:
            subprocess.call(['less', self.filename])
        except Exception as e:
            self.write(str(e), traceback=e)
            return

    def clear(self):
        open(self.filename, 'w').close()
        #print "Logfile cleared."
        print("Logfile cleared.")


def write(mes=None, traceback=None):
    return Log.get().write(mes, traceback)

def view():
    return Log.get().view()

def clear():
    return Log.get().clear()
