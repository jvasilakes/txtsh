import subprocess

import pager

from header import *
from dict_methods import getMaxKey


def _drop(*args):

    return STOP


def _words(*args):

    text_object = args[0]

    if not text_object.words:
	print "This text object contains no words."
	return GO

    print "\nNumber of distinct words: %d" % len(text_object.words.keys())

    (word, count) = getMaxKey(text_object.words)
    print "\nMost common word: %s (%d occurrences)" % (word, count)

    print "\nDisplay all distinct words? [y/n]: ",
    ans = raw_input()

    if ans.lower() == 'y':

	words = "--- DISTINCT WORDS ---\n\n%s" % str(sorted(text_object.words.keys()))

	if len(sorted(text_object.words.keys())) > 300:
	    pager.page(words)

	else:
	    print words

    else:
	pass

    return GO


def _punct(*args):

    text_object = args[0]

    if not text_object.punctuation:
	print "This text object contains no punctation."
	return GO

    print "\nDistinct punctuation: %s" % str(text_object.punctuation.keys())

    print "\nNumber of distinct punctation: %d\n" % len(text_object.punctuation.keys())

    return GO


def _nums(*args):

    text_object = args[0]

    if not text_object.numbers:
	print "This text object contains no numbers."
	return GO

    print "\nDistinct numbers: %s" % str(text_object.numbers.keys())

    print "\nNumber of distinct numbers: %d\n" % len(text_object.numbers.keys())

    return GO


def _hist(*args):

    text_object = args[0]

    if not text_object.contents:
	print "Could not read contents of text object."
	return GO

    if text_object.filepath is not None:
	subprocess.call(['hist', text_object.filepath])

    else:
	subprocess.call(['hist', text_object.contents])

    return GO
    

map = {
    '!drop': _drop,
    '!words': _words,
    '!punct': _punct,
    '!nums': _nums,
    '!hist': _hist
      }

