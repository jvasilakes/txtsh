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
        self.history = '.txtsh_history'

    def _exec(self, arg, data_object=None):
        """
        Parse command-line input and execute
        the command, if present.
        """

        if not arg:
            return GO

        with open(self.history, 'a') as fp:
            fp.write(arg + '\n')

        if not self.is_command(arg, self.cmd_set):
            print(arg)
            return GO

        args = self.findArgs(arg)
        if self.VERBOSE:
            print(args)

        if data_object:
            args.insert(1, data_object)

        if len(args) == 1:
            status = self.cmd_set.map[args[0]]()
        elif len(args) > 1:
            status = self.cmd_set.map[args[0]](*args[1:])
        else:
            status = GO

        return status

    def import_cmd_set(self):
        """
        Import the correct command set for
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

    def is_command(self, arg, commands):
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

    def findArgs(self,cmd):

        strings = re.search(r'([\'"])(?P<string>[^\1]+)\1', cmd)

        if strings:
            strings = strings.group('string')
            strings = [strings]
        else:
            strings = []

        args = re.match(r'![^\'"]+', cmd).group(0)
        args = args.split()
        args.extend(strings)

        return args
