#! /usr/bin/python2

from __future__ import division


def estimate_probs(trigram_counts_dict):
    '''
    Estimates probabilities (MLE) of trigrams using
    trigram_counts_dict and returns a new dictionary
    with the probabilities.
    '''
    trigram_probs_dict = trigram_counts_dict.copy()
    
    for key, value in trigram_counts_dict.items():

        # Calculate value of trigram based on counts
        # of the bigram that begins it.
    	bigrams = [trigram_counts_dict[k] for k in trigram_counts_dict.keys()
                   if k.startswith(key[:len(key)-1])]
    	trigram_probs_dict[key] = value/sum(bigrams)
    return trigram_probs_dict
