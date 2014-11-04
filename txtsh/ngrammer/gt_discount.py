#! /usr/bin/python

from __future__ import division
import collections


def gt_discount(tri_counts):
    '''
    # Good-Turing discounter.
    # Calculates Good-Turing probability of
    # zero-count trigrams, and discounts
    # all counts in tri_counts accordingly.
    # Recasts tri_counts as a defaultdict with
    # zero_count_probs as the default value.
    '''

    # Calculate the probability for trigrams with zero count.
    N_1 = len([i for i in tri_counts.itervalues() if i == 1])
    N = sum(tri_counts.values())
    zero_count_probs = (N_1 / N)

    # Calculate updated counts and update values.
    for key, value in tri_counts.iteritems():
        num1 = value + 1

        if not num1 in tri_counts.values():
            pass

        else:
            num2 = len([n for n in tri_counts.itervalues() if n == num1])
            denom = len([n for n in tri_counts.itervalues() if n == value])

            # Update value with the new count
            tri_counts[key] = (num1 * num2) / denom

    # Cast tri_counts as a defaultdict with zero_count_probs as the default
    # value. Default values used in calc_perplexity.
    new_counts = collections.defaultdict(lambda: zero_count_probs, tri_counts) 

    return new_counts
