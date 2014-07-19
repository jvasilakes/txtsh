def getMaxKey(d):

    if not isinstance(d, dict):
	print "Input must be a dictionary."

    word = d.keys()[0]

    count = 0

    for key in d:
	if d[key] > count:
	    count = d[key]
	    word = key

    return word, count

