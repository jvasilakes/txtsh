from __future__ import print_function

def getMaxKey(d):
    """
    Find the key with the maximum value in a dictionary
    and return the key, value pair.
    """

    if not isinstance(d, dict):
        print("Input must be a dictionary.")

    temp = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return temp[0][0], temp[0][1]
