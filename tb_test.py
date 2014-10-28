import sys, traceback

def exc():
    try:
        c = []
        b = c[6]
    except:
        print "YESSSS"
        t, val, tb = sys.exc_info()
        lines = traceback.format_exc().splitlines()
        print lines[-1]
        print tb.tb_lineno

exc()
