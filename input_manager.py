from importlib import import_module

from header import *


class InputManager(object):

    def __init__(self, shell):

        self.shell = shell


    def manage(self, input):

        if not input:

            return GO

	else:

            status = self._exec(input)

            return status


    def is_command(self, input, commands):

        args = input.split()

        if args[0].startswith('!'):
	    if args[0] in commands.map.keys():

		return True

	    else:
		print "'%s' is not a valid command." % args[0]
		return False

        else:
            return False 


    def findArgs(self, input):

        args = input.split(None, 1)

        if len(args) == 1:
            return args

	else:

	    if args[1].startswith('"') or args[1].startswith("'"):
		
		if args[1].startswith('"'):
		    quote_type = '"'

		elif args[1].startswith("'"):
		    quote_type = "'"

		valid_quotes = False

		if args[1].endswith(quote_type):
		    valid_quotes = True

		if valid_quotes == False:
		    print "Syntax error!"
		    return

		temp = args[1].split(quote_type)
		    
		for item in temp:
		    if item:
			args[1] = item

			return args

	    else:

		return args


    def _exec(self, input):

	sh_type = self.shell.getType

	if sh_type == 'Shell':
	    cmds = import_module('command_shell')

	elif sh_type == 'Subshell':
	    cmds = import_module('command_subshell')

	else:
	    print "Error: Invalid shell!"
	    return

	if not self.is_command(input, cmds):
	    return

	args = self.findArgs(input)

	try:
	    return cmds.map[args[0]]()

	except TypeError:

	    rest = ''.join(args[1:])
	    return cmds.map[args[0]](rest)	

