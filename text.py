from sys import exit


class Text(object):

    members = []

    def __init__(self):

	self.id = self.set_id()

	self.string = ''

	self.words = {}

	self.numbers = {}

	self.members.append(self)

    
    def throwError(self, error_message="Generic error"):

	print error_message

	exit(1)


    def set_id(self):
    
	if self.members:
	    return (self.members[(len(Text.members) - 1)].id) + 1

	else:
	    return 1


    def load_data(self, data):

	self.string = data

	temp = data.split()

	for item in temp:

	    if item.isalpha():
		list = self.words
	    elif item.isdigit():
		list = self.numbers
	    else:
		self.throwError("Strings must be alpha-numeric!")

	    if item in list:
		list[item] += 1
	    else:
		list.update({item: 1})

	print "Load successful."


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

