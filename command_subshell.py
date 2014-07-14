from header import *


def _drop(*args):

    return STOP


def _words(*args):

    args = args[0]
    text_object = args[0]

    if not text_object.words:
	print "This text object contains no words."
	return GO

    print "\nDistinct words: %s" % str(sorted(text_object.words.keys()))

    print "\nNumber of distinct words: %d\n" % len(text_object.words.keys())

    return GO


def _punct(*args):

    args = args[0]
    text_object = args[0]

    if not text_object.punctuation:
	print "This text object contains no punctation."
	return GO

    print "\nDistinct punctuation: %s" % str(text_object.punctuation.keys())

    print "\nNumber of distinct punctation: %d\n" % len(text_object.punctuation.keys())

    return GO


def _nums(*args):

    args = args[0]
    text_object = args[0]

    if not text_object.numbers:
	print "This text object contains no numbers."
	return GO

    print "\nDistinct numbers: %s" % str(text_object.numbers.keys())

    print "\nNumber of distinct numbers: %d\n" % len(text_object.numbers.keys())

    return GO

    
map = {
    '!drop': _drop,
    '!words': _words,
    '!punct': _punct,
    '!nums': _nums
      }

