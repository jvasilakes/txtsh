from importlib import import_module

import command

from header import *


class InputManager(object):

    def __init__(self, shell):

        self.shell = shell


    def manage(self, input):

        if not input:

            return GO

        elif self.is_command(input):

            status = self._exec(input)

            return status

        else:

            return GO


    def is_command(self, input):

        args = input.split()

        if args[0].startswith('!'):
	    if args[0] in command.map.keys():

		return True

	    else:
		print "'%s' is not a valid command." % args[0]

        else:
            return False 


    def findArgs(self, input):

        args = input.split(None, 1)

        if len(args) == 1:
            return args

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

        cmds = import_module('command')

	args = self.findArgs(input)

	try:
	    return cmds.map[args[0]]()

	except TypeError:

	    rest = ''.join(args[1:])
	    return cmds.map[args[0]](rest)	

