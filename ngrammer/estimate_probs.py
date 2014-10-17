#! /usr/bin/python2

# from the __future__ package, import division
# to allow float division

from __future__ import division


def estimate_probs(trigram_counts_dict):
    '''
    # Estimates probabilities (MLE) of trigrams using
    # trigram_counts_dict and returns a new dictionary
    # with the probabilities.
    '''
    
    # variable that creates a new dictionary called
    # trigram_probs_dict which is a copy of trigram_counts_dict.
    trigram_probs_dict = trigram_counts_dict.copy()
    
    # a for loop that iterates over all the keys in trigram_probs_dict.
    # within this for loop, we iterate over all keys again with k
    # and if that key 'k' starts with the same two characters as key
    # the value of that key is stored. sum(bigrams) is te sum of all these values.
    # It's the frequency of bigram key[:2], i.e., the first two characters of key.
    # The probability is then computed by dividing the value of key by the frequency
    # of the first two characters of key.
    # Once all keys are iterated over, trigram_probs_dict is returned
    for key, value in trigram_counts_dict.items():
    	#bigrams = [trigram_counts_dict[k] for k in trigram_counts_dict.keys() if k.startswith(key[:2])]
    	bigrams = [trigram_counts_dict[k] for k in trigram_counts_dict.keys() if k.startswith(key[:len(key)-1])]
    	trigram_probs_dict[key] = value / sum(bigrams)
    return trigram_probs_dict
    
#--------------------------------------------------------#
'''
# This is a test string
'''

if __name__ == '__main__':
	s = {
	' a ': 1, 's i': 1, 'his': 1, 'str': 1, 's a': 1,
	' is': 1, 'ing': 1, ' st': 1, 'rin': 1, 'tri': 1, 'thi': 1,
	'a s': 1, 'is ': 2
	}
	
	print estimate_probs(s)
