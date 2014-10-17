#! /usr/bin/python2

from __future__ import division

import numpy


# JAKE
def calc_perplexity(test_counts_dict, trigram_probs_dict):
    '''
    # Calculates perplexity of contents of file_string
    # according to probabilities in trigram_probs_dict.
    '''

    test_probs = []

    for trigram, count in test_counts_dict.items():

        for n in range(count):
            logprob = numpy.log2(trigram_probs_dict[trigram])
            test_probs.append(logprob)

    logprob = sum(test_probs)

    entropy = logprob / len(test_probs)

    perplexity = numpy.power(2, -entropy)

    return perplexity
