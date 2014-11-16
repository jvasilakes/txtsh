from __future__ import print_function

import inspect
import re
from importlib import import_module

from txtsh.header import *


class InputManager(object):
    """
    The interpreter for the txtsh shell.
    """

    def __init__(self, shell, verbose=False):

        self.VERBOSE = verbose
        self.shell = shell
        self.cmd_set = self.import_cmd_set()
        self.history = []

    def manage(self, arg, data_object=None):
        """
        Parse command-line input and execute
        the command, if present.
        """
        if not self.is_command(arg, self.cmd_set):
            print(arg)
            return GO

        args = self.parseArgs(arg)

        # For Subshells. If we're dealing with a 
        # loaded text object, make sure it's an
        # argument to the command.
        if data_object:
                args.insert(1, data_object)

        # If it's a valid command
        # save it in the history.
        self.addToHistory(args)

        if self.VERBOSE:
            print(args)

        return self._exec(args)

    def _exec(self, args):
        """
        Execute the command contained within args.
        """
        if len(args) == 1:
            status = self.cmd_set.map[args[0]]()
        elif len(args) > 1:
            status = self.cmd_set.map[args[0]](*args[1:])
        else:
            status = GO

        return status

    def import_cmd_set(self):
        """
        Import the correct commands for
        the given shell type.
        """

        sh_type = self.shell.Type

        if sh_type == 'Shell':
            cmds = import_module('txtsh.commands.cmd_shell')
        elif sh_type == 'Subshell':
            cmds = import_module('txtsh.commands.cmd_subshell')
        else:
            raise Exception("BadSh: Invalid shell!")

        return cmds

    def addToHistory(self, args):
        self.history.append(args)

    def is_command(self, arg, commands):
        """
        Checks if the input is a valid
        according to the imported command set.
        """
        arg = arg.strip().lower()
        args = arg.split(None, 1)

        if args[0].startswith('!'):

            if args[0] in commands.map.keys():
                return True
            else:
                print("'{}' is not a valid command." .format(args[0]))
                return False
        else:
            return False

    def parseArgs(self,cmd):
        """
        Parses the raw input into a list of arguments.
        """

        strings = re.search(r'([\'"])(?P<string>[^\1]+?)\1', cmd)

        if strings:
            strings = strings.group('string')
            strings = [strings]
        else:
            strings = []

        args = re.match(r'![^\'"]+', cmd).group(0)
        args = args.split()
        args.extend(strings)

        return args
