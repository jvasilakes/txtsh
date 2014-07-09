import shell

from header import *
from text import Text


def _quit():

    return STOP


def _help():

    print "\r"

    print "--- Available commands ---"
    print "!help: display this help screen."
    print "!quit: quit the shell."
    print "!info: display version information."
    print "!load STRING: load STRING into database."
    print "!free ID: unload object stored in ID."
    print "!list: print all loaded objects."
    print "!use ID: go to subshell to manipulate data stored in ID."
    print "!drop: Drop out of subshell created by '!use'."

    print "\r"

    return GO


def _info():

    print "TXTSH Text Analysis Shell (ver. 0.0) running on %s." % PLATFORM
    print "Type '!help' for a list of commands."

    return GO
    

def _load(string):

    new = Text()    

    try:
	new.load_data(string)

	return GO

    except:
	return STOP


def _free(id):

    id = int(id)

    object = None

    for member in Text.members:
	if member.id == id:

	    object = member 

    if not object:
	print "No object found with id '%d'." % id
	return GO

    Text.members.remove(object)

    return GO


def _list():

    if len(Text.members) == 0:
	print "No objects loaded."
    
    else:
	print "ID\tSAMPLE\n"

	for member in Text.members:
	    print '%2s' % member.id,
	    print '\t',
	    print '"%s"' % member.title

    return GO


def _use(id):

    id = int(id)

    object = None

    for member in Text.members:
	if member.id == id:

	    object = member 

    if not object:
	print "No object found with id '%d'." % id
	return GO

    subsh = shell.Subshell(object)
    subsh.run()

    return GO


# ---- MAPPINGS -----

map = {
    '!quit': _quit, \
    '!help': _help, \
    '!info': _info, \
    '!load': _load, \
    '!free': _free, \
    '!list': _list, \
    '!use': _use
       }

