from __future__ import print_function

def getMaxKey(d):

    if not isinstance(d, dict):
        #print "Input must be a dictionary."
        print("Input must be a dictionary.")

    temp = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return temp[0][0], temp[0][1]
