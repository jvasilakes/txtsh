#! /usr/bin/python2

from collections import defaultdict


def count_ngrams(n, data):

    counts = defaultdict(int)

    i = 0
    j = n

    for char in data:
        counts[tuple(data[i:j])] += 1
        i+=1
        j+=1

    return counts
