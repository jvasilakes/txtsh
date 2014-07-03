from sys import exit


class Text(object):

    members = []

    def __init__(self):

	self.id = self.set_id()

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


    def find_punctuation(self, data_list):

	pass

	"""
	if not isinstance(data_list, list):
	    return

	else:
	    punct = []


	    for item in data_list:
    
		if not item.isalnum():
	"""


    def load_data(self, data):

	self.string = data

	temp = data.split()

	for item in temp:

	    if item.isalpha():
		l = self.words
	    elif item.isdigit():
		l = self.numbers
	    else:
		self.throwError("Input must be alpha-numeric!")

	    if item in l:
		l[item] += 1
	    else:
		l.update({item: 1})

	print "String loaded into id %d." % self.id


    def overview(self):

	print '"%s"' % self.string

	if self.words:
	    print "Distinct words: %d" % len(self.words)
    
	if self.numbers:
	    print "Distinct numbers: %d" % len(self.numbers)

	"""
	if len(parsed_text) == 1:
	    print "'%s'" % parsed_text[0]

	elif len(parsed_text) == 2:
	    print "'%s' and '%s'." % (parsed_text[0], parsed_text[1])

	elif len(parsed_text) > 2:
	    for word in parsed_text[:(len(parsed_text) - 1)]:
		    print "'%s'," % word.rstrip(),

	    print "and '%s'." % parsed_text[len(parsed_text) - 1]

	else:
	    return
	"""

