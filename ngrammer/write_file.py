#! /usr/bin/python2

# Imports only needed for test function.
import string
import math
import random
import os
import errno


def test(write_func):
    '''
    # Generate a dummy dictionary of trigrams
    # with random probabilities.
    '''

    # Generate dummy trigram probability model.
    alphabet = list(string.ascii_lowercase)

    random.seed()

    test_dict = {}

    # These probabilities will likely not add up to 1.
    for i in xrange(random.randint(100, 300)):
        trigram = ''.join(random.sample(alphabet, 3))
        prob = math.pow(random.random(), random.randint(5, 8))
        test_dict.update({trigram: prob})

    # Test the write_file function with the dummy model.
    write_func(test_dict)

    return "Write succeeded."


# JAKE
def write_file(trigram_probs_dict, model_name=None):
    '''
    # Writes nicely formatted contents
    # of trigram_probs_dict to a file,
    # called trigram_model.txt. If the file
    # already exists, each new model is
    # appended to the end of the file.
    '''

    # Default model_name
    if not model_name:
        model_name = "UNTITLED MODEL"
    else:
        model_name = model_name.upper()

    # Open trigram_model.txt (create it if it doesn't exist)
    # in append mode.
    with open('trigram_model.txt', 'a') as f:

        # Write the model_name and column headers
        f.write(" \t\t**** {0} ****\n\n" .format(model_name))

        # Write the contents of the trigram model
        entries = 0
        for key, value in sorted(trigram_probs_dict.items()):
            f.write("  {0}  :  {1},  " .format(key, value))

            if entries == 5:
                f.write('\n')
                entries = 0
            else:
                entries += 1

        f.write('\n\n\n')

    return


if __name__ == '__main__':
    print test(save_model)
