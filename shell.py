from header import *
from input_manager import input_manager


class Shell(object):

    members = []

    def __init__(self):

	self.PROMPT = '**>'

	# current subshell (or lack thereof)
	self.current = self

	self.state = GO

	self.cmd = None

	self.addToMembers()

	
    def addToMembers(self):

	if not isinstance(self, Subshell):
	    for shell in self.members:
		if not isinstance(shell, Subshell):

		    try:
			raise Exception("Only one main shell allowed.")

		    except:
			return		

	self.members.append(self)

	
	    
    def run(self):

	while self.state == GO:

		print self.PROMPT,

		self.cmd = raw_input()

		self.state = input_manager(self.cmd)


class Subshell(Shell):

    def __init__(self, data_object):

	Shell.__init__(self)

	self.data = data_object

	self.PROMPT = '[using: %d]>' % self.data.id

    
    def run(self):

	#dummy run for now

	while self.state == GO:

	    print self.PROMPT,

	    self.cmd = raw_input()

	    if self.cmd == '!drop':
		#self.state == STOP
		break

	    else:
		self.cmd = raw_input()

	del self
