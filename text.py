from sys import exit

import nltk


class Text(object):

    members = []

    def __init__(self):

	self.id = self.set_id()

	self.title = ''

	self.string = ''

	self.words = {}

	self.numbers = {}

	self.punctuation = {}

	self.members.append(self)

    
    def throwError(self, error_message="Generic error"):

	print error_message

	return


    def set_id(self):
    
	if self.members:
	    return (self.members[(len(Text.members) - 1)].id) + 1

	else:
	    return 1


    def load_data(self, data):

	self.title = data[:20]

	self.string = data

	temp = nltk.word_tokenize(data)

	for item in temp:

	    if item[0].isalpha():
		l = self.words
	    elif item.isdigit():
		l = self.numbers
	    else:
		l = self.punctuation

	    if item in l:
		l[item] += 1
	    else:
		l.update({item: 1})

	print "String loaded into id %d." % self.id


    def overview(self):

	print '"%s"' % self.title

	if self.words:
	    print "Distinct words: %d" % len(self.words)
    
	if self.numbers:
	    print "Distinct numbers: %d" % len(self.numbers)

