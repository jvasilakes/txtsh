import command

from header import *


def input_manager(input):

    if not input:

	return GO

    elif is_command(input):

	status = _exec(input)

	return status

    else:

	parsed = parse_text(input)

	display_text(parsed)

	return GO


def is_command(input):

    args = input.split()

    if args[0].startswith('!'):
	return True

    else:
	return False 


def findArgs(input):

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

	temp = args.pop(1)

	args.extend(temp.split())

	return args
    

def _exec(input):

    args = findArgs(input)

    if args[0] == '!quit':
    
	command._quit()

	return STOP

    elif args[0] == '!help':

	command._help()

	return GO

    elif args[0] == '!info':

	command._info()

	return GO

    elif args[0] == '!load':

	if len(args) != 2:
	    print "Syntax error: !load takes one argument."

	command._load(args[1])

	return GO

    elif args[0] == '!list':

	command._list()

	return GO

    else:
	
	return GO


# -------- 2 B DEPRECATED ----------------------------------

def parse_text(text):

	parsed = text.split(' ')

	return parsed


def display_text(parsed_text):

	print "You entered %d distinct words:" % len(parsed_text)

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

