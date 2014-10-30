#! /usr/bin/python2

import numpy as np
import collections

def gen_random_output(ngram_probs_dict, n=300):
        '''
        # Generate n characters of output randomly selected
        # from the keys of ngram_probs_dict. 
        # OrderedDict is used to ensure that each key is 
        # paired with its associated value.
        '''

        # Start from the end of some pretend previous sentence.
        random_string = ". "
        
        for i in range(n):
        	od = collections.OrderedDict()
        	for key, value in ngram_probs_dict.iteritems():
        		if key.startswith(random_string[-2:]):
        			od.update({key: value})
        	next = np.random.choice(od.keys(), p=od.values())

                # Just append the last character of the trigram.
        	random_string += next[-1]
        
        return random_string
