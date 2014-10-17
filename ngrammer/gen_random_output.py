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
        random_string = np.random.choice(ngram_probs_dict.keys())
        
        for i in range(n):
        	od = collections.OrderedDict()
        	for key, value in ngram_probs_dict.iteritems():
        		if key.startswith(random_string[-2:]):
        			od.update({key: value})
        	next = np.random.choice(od.keys(), p=od.values())
        	random_string += next[-1]
        
        return random_string


# --------------------------------------------------------#
'''
# This is a test string
'''

if __name__ == '__main__':
        s = {
            'tri': 0.07142857142857142, 's i': 0.07142857142857142,
            'rin': 0.07142857142857142, 'his': 0.07142857142857142,
            'thi': 0.07142857142857142, 'str': 0.07142857142857142,
            's a': 0.07142857142857142, ' a ': 0.07142857142857142,
            'is ': 0.07142857142857142, 'ing': 0.07142857142857142,
            'a s': 0.07142857142857142, ' is': 0.07142857142857142,
            ' st': 0.14285714285714285
        }
