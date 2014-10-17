#! /usr/bin/python2


def count_trigrams(n, processed_string):
#def count_trigrams(processed_string):
        '''
        # The function count_trigrams counts all
        # character trigrams in processed_string
        # and creates a dictionary of those trigram counts
        # called trigram_counts_dict.
        '''

        # This empty dictionary will be filled with
        # the trigrams in processed_string and their frequencies
        trigram_counts_dict = {}

        # i and j are set to the start positions of
        # the indices within processed_string
        # (print s[0:3] prints the first three characters of s)
        i = 0
        j = n

        # this for loop iterates over the characters
        # in processed_line, pairs them into trigrams
        # and increments the count of the indices i and j.
        # If the resulting trigram is a key in trigram_counts_dict,
        # the value is incremented by 1.
        # If the trigram is not a key in trigram_counts_dict,
        # a key is added with value 1.
        # Once there are no more trigrams to be iterated over,
        # trigram_counts_dict is returned.
        for char in processed_string:
                if len(processed_string[i:j]) == n:
                        trigram = processed_string[i:j]
                        i += 1
                        j += 1
                        if trigram in trigram_counts_dict:
                                trigram_counts_dict[trigram] += 1
                        else:
                                trigram_counts_dict[trigram] = 1
        return trigram_counts_dict

# --------------------------------------------------------#
'''
# This is a test string
'''

if __name__ == '__main__':
        s = "this is a string"
        print count_trigrams(s)
