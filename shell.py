from header import *
from input_manager import input_manager


class Shell(object):

    members = []

    def __init__(self):

	self.state = GO

	self.cmd = None

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

		print PROMPT,

		self.cmd = raw_input()

		self.state = input_manager(self.cmd)


class Subshell(Shell):

    def __init__(self, data_object):

	Shell.__init__(self)

	self.data = data_object

    
