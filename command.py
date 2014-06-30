from text import Text


def _quit():

    print "Leaving this horrible shell..."


def _help():

    print "--- Available commands ---"
    print "!help: display this help screen."
    print "!quit: quit the shell."
    print "!info: display version information."
    print "!load STRING: load STRING into database."
    print "!list: print all loaded objects."

    return


def _info():

    print "txtsh Text analysis shell (ver. 0.0)"
    print "Type '!help' for a list of commands."
    

def _load(string):

    new = Text()    

    new.load_data(string)


def _list():

    if len(Text.members) == 0:
	print "No objects loaded."
    
    else:
	print "ID\tSAMPLE\n"

	for member in Text.members:
	    print '%2s' % member.id,
	    print '\t',
	    print '"%s"' % member.string


def _use(id):

    pass
    # Launch subshell in which user can manipulate
    ## data belonging to id
