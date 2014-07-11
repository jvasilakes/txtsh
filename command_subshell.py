from header import *


def _drop(data_object):

    return STOP


def _words(data_object):

    if not data_object.words:
	print "\nThis data object has no words."
	return GO

    print "\nDistinct words: %s" % str(sorted(data_object.words.keys()))

    print "\nNumber of distinct words: %d\n" % len(data_object.words.keys())

    return GO


def _punct(data_object):

    if not data_object.punctuation:
	print "\nThis data object has no punctation."
	return GO

    print "\nDistinct punctuation: %s" % str(data_object.punctuation.keys())

    print "\nNumber of distinct punctation: %d\n" % len(data_object.punctuation.keys())

    return GO

map = {
    '!drop': _drop,
    '!words': _words,
    '!punct': _punct
      }

