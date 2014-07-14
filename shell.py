from header import *
from input_manager import InputManager


class Shell(object):

    members = []

    def __init__(self):

	self.PROMPT = 'TXTSH>'

	self.input_manager = InputManager(self)

	self.state = GO

	self.cmd = None

	self.addToMembers()


    # Returns shell's type as a string. Used within _exec()
    @property
    def getType(self):

	temp = str(type(self))

	return temp.rsplit('.')[-1][:-2]

	
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

	self.input_manager._exec('!info')

	while self.state == GO:

		print self.PROMPT,

		self.cmd = raw_input()

		self.state = self.input_manager._exec(self.cmd)

	while self.state == STOP:

		print "Thx 4 using txtsh!!!"

		break


class Subshell(Shell):

    def __init__(self, data_object):

	Shell.__init__(self)

	self.data = data_object

	self.PROMPT = 'ID: %d>' % self.data.id

    
    def run(self):

	while self.state == GO:

		print self.PROMPT,

		self.cmd = raw_input()

		self.state = self.input_manager._exec(
						    self.cmd,
						    data_object=self.data
						     )

	del self
