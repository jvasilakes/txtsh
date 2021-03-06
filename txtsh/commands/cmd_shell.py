from __future__ import print_function

import sys
import os
import subprocess

import txtsh.shell as shell
import txtsh.file_explorer as file_explorer
import txtsh.log as log
import txtsh.pager as pager

from txtsh.text import Text
from txtsh.header import *


def _help(*args):

    pager.page('README.md')

    return GO


def _info(*args):

    print("TXTSH Text Analysis Shell (ver. 0.0) on {}." .format(PLATFORM))
    print("Type '!help' for a list of commands.")

    return GO


def _log(*args):

    if len(args) > 0:
        if args[0] == 'clear':
            log.clear()
        else:
            print("Unknown command to log: '{}'" .format(args[0]))

    else:
        log.view()

    return GO


def _load(*args):

    """
    data_type must be either 'string' or 'file'.

    If data_type is 'string', data will be
    loaded verbatim into a new Text object.

    If data_type is 'file', it will attempt to
    open the data as a read-only text file and
    load its contents into a new Text object.

    A file explorer will launch if file data is not provided.

    """

    if len(args) < 1:
        print("Error: load takes at least one argument.")
        return GO

    data_type = args[0]

    if data_type != 'string' and data_type != 'file':
        print("Error: you must specify 'string' or 'file'")
        return GO

    if len(args) != 2 and data_type == 'string':
        print("Error: you must provide a single string to load.")
        return GO

    if len(args) == 1 and data_type == 'file':
        explorer = file_explorer.Explorer()
        data = explorer.navigate()

        if data is None:
            print("Error: must provide a data file to load.")
            return GO

    else:
        data = args[1]

    new = Text()

    try:
        new.load_data(data_type, data)

        return GO

    except Exception:
        log.write(traceback=True)
        print("Loading text data failed.")

        return GO


def _free(*args):

    id_num = int(args[0])

    obj = None

    for member in Text.members:
        if member.id_num == id_num:

            obj = member

    if not obj:
        print("No object found with id '{}'." .format(id_num))
        return GO

    Text.members.remove(obj)

    return GO


def _list(*args):

    if len(Text.members) == 0:
        print("No objects loaded.")

    else:
        print("ID\tSAMPLE\n")

        for member in Text.members:
            print('%2s' % member.id_num, end="")
            print('\t', end="")
            print('"{}"' .format(member.title))

    return GO


def _use(*args):

    try:
        id_num = int(args[0])
    except:
        print("Error: must specify an ID number.")
        return GO

    obj = None

    for member in Text.members:
        if member.id_num == id_num:

            obj = member

    if not obj:
        print("No object found with id '{}'." .format(id_num))
        return GO

    subsh = shell.Subshell(obj)
    subsh.run()

    return GO


def _quit(*args):

    # Cleanup memory for any loaded objects
    for i in reversed(range(len(Text.members))):
        _free(Text.members[i].id_num)

    return STOP


def _restart(*args):

    ans = raw_input("Restart txtsh? All loaded objects will be freed! [y/n]: ")
    if ans.lower().strip() == 'y':

        print("\nRestarting...\n")

        # Cleanup memory for any loaded objects
        for i in reversed(range(len(Text.members))):
            _free(Text.members[i].id_num)

        python = sys.executable

        os.execl(python, python, * sys.argv)

    else:
        return GO


def _update(*args):

    print("Don't use this...")
    return GO

    print("Updating txtsh...")

    try:
        os.chdir(TXTSH_HOME_DIR)
        p = subprocess.Popen(['git', 'pull', 'origin', 'master'])
        code = p.wait()

        if code == 0:
            print("Update complete.")
            print("If changes were made, restart \
                    (!restart) txtsh for changes to take effect.")

        else:
            print("Update failed.")

    except:
        print("Update command failed to execute.")

    return GO


# ---- MAPPINGS -----

map = {
    '!help': _help,
    '!info': _info,
    '!log': _log,
    '!load': _load,
    '!free': _free,
    '!list': _list,
    '!use': _use,
    '!quit': _quit,
    '!restart': _restart,
    '!update': _update
       }
