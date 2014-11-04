from __future__ import print_function

import subprocess

import txtsh.pager as pager
from txtsh.header import *
from txtsh.dict_methods import getMaxKey


def _drop(*args):

    return STOP


def _print(*args):

    text_object = args[0]

    if len(sorted(text_object.words.keys())) > 300:
        pager.page(text_object.contents)
    else:
        print(text_object.contents)

    return GO

def _words(*args):

    text_object = args[0]

    if not text_object.words:
        print("This text object contains no words.")
        return GO

    print("\nNumber of distinct words: {}"
          .format(len(text_object.words.keys())))

    (word, count) = getMaxKey(text_object.words)
    print("\nMost common word: {0} ({1} occurrences)" .format(word, count))

    print("\nDisplay all distinct words? [y/n]: "),
    ans = raw_input()

    if ans.lower() == 'y':

        words = "--- DISTINCT WORDS ---\n\n{}" \
                .format(str(sorted(text_object.words.keys())))

        if len(sorted(text_object.words.keys())) > 300:
            pager.page(words)

        else:
            print(words + '\n')

    else:
        pass

    return GO


def _punct(*args):

    text_object = args[0]

    if not text_object.punctuation:
        print("This text object contains no punctation.")
        return GO

    print("\nDistinct punctuation: {}"
          .format(str(text_object.punctuation.keys())))

    print("\nNumber of distinct punctation: {}\n"
            .format(len(text_object.punctuation.keys())))

    return GO


def _nums(*args):

    text_object = args[0]

    if not text_object.numbers:
        print("This text object contains no numbers.")
        return GO

    print("\nDistinct numbers: {}" .format(str(text_object.numbers.keys())))

    print("\nNumber of distinct numbers: {}\n"
            .format(len(text_object.numbers.keys())))

    return GO


def _hist(*args):

    text_object = args[0]

    if not text_object.contents:
        print("Could not read contents of text object.")
        return GO

    if text_object.filepath is not None:
        subprocess.call(['hist', text_object.filepath])

    else:
        subprocess.call(['hist', text_object.contents])

    return GO
    

map = {
    '!drop': _drop,
    '!print': _print,
    '!words': _words,
    '!punct': _punct,
    '!nums': _nums,
    '!hist': _hist
      }
