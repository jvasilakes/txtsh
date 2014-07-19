import os, subprocess

import shell

from header import *
from text import Text


def _quit(*args):

    return STOP


def _update(*args):

    print "Updating txtsh..."

    os.chdir(TXTSH_HOME_DIR)
    p = subprocess.Popen(['git', 'pull', 'origin', 'master', '&'])
    code = p.wait()

    if code == 0:
	print "Update complete. Restart txtsh for changes to take effect."

    else:
	print "No update available."

    return GO


def _help(*args):

    print "\r"

    print "--- Main shell commands ---"
    print "!help: display this help screen."
    print "!quit: quit the shell."
    print "!info: display version information."
    print "!update: update txtsh to the latest version."
    print "!load DATA_TYPE, DATA: load DATA into database. DATA_TYPE must be 'string' or 'file'."
    print "!free ID: unload text object stored in ID."
    print "!use ID: go to subshell to manipulate text data stored in ID."
    print "!list: print all loaded objects."

    print "\n--- Subshell commands ---"
    print "!drop: Drop out of subshell created by '!use'."
    print "!words: Display word data for loaded text."
    print "!punct: Display punctuation data for loaded text."
    print "!nums: Display number data for loaded text." 

    print "\r"

    return GO


def _info(*args):

    print "TXTSH Text Analysis Shell (ver. 0.0) on %s." % PLATFORM
    print "Type '!help' for a list of commands."

    return GO
    

def _load(*args):

    """
    data_type must be either 'string' or 'file'.

    If data_type is 'string', data will be
    loaded verbatim into a new Text object.

    If data_type is 'file', it will attempt to
    open the data as a read-only text file and
    load its contents into a new Text object.

    """
    
    data_type = args[0]
    data = args[1]

    if data_type != 'string' and data_type != 'file':
	print "Error: you must specify 'string' or 'file'"
	return GO

    new = Text()    

    try:
	new.load_data(data_type, data)

	return GO

    except:
	print "Loading text data failed."

	return GO


def _free(*args):

    id = int(args[0])

    object = None

    for member in Text.members:
	if member.id == id:

	    object = member 

    if not object:
	print "No object found with id '%d'." % id
	return GO

    Text.members.remove(object)

    return GO


def _list(*args):

    if len(Text.members) == 0:
	print "No objects loaded."
    
    else:
	print "ID\tSAMPLE\n"

	for member in Text.members:
	    print '%2s' % member.id,
	    print '\t',
	    print '"%s"' % member.title

    return GO


def _use(*args):

    id = int(args[0])

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
    '!quit': _quit,
    '!update': _update,
    '!help': _help,
    '!info': _info,
    '!load': _load,
    '!free': _free,
    '!list': _list,
    '!use': _use
       }

