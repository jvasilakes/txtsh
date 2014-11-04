from __future__ import print_function

import inspect
from importlib import import_module

from txtsh.header import *


class InputManager(object):
    """
    The interpreter for the txtsh shell.
    """

    def __init__(self, shell):

        self.shell = shell
        self.cmd_set = self.import_cmd_set()

    def _exec(self, arg, data_object=None):
        """
        Parse command-line input and execute
        the command, if present.
        """

        if not arg:
            return GO

        cmd = arg.strip().lower()

        if not self.is_command(cmd, self.cmd_set):
            print(arg)
            return GO

        args = self.findArgs(cmd)

        if data_object is not None:
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

        sh_type = self.shell.getType

        if sh_type == 'Shell':
            cmds = import_module('txtsh.commands.cmd_shell')
        elif sh_type == 'Subshell':
            cmds = import_module('txtsh.commands.cmd_subshell')
        else:
            print("Error: Invalid shell!")
            return

        return cmds

    def is_command(self, cmd, commands):
        args = cmd.split(None, 1)

        if args[0].startswith('!'):
            if args[0] in commands.map.keys():
                return True
            else:
                print("'{}' is not a valid command." .format(args[0]))
                return False
        else:
            return False

    def findArgs(self, cmd):
        """
        Find the arguments and handle
        quoted strings.
        """
        args = cmd.split()

        if len(args) == 1:
            return args
        else:
            quote_found = False
            valid_quotes = False

            for arg in args:
                if arg.startswith('"'):
                    quote_found = True
                    start_idx = args.index(arg)

                    for arg in args[start_idx:]:
                        if arg.endswith('"'):
                            valid_quotes = True
                            end_idx = args.index(arg)
                            break

            # Return with error if valid quotation was not used.
            if quote_found:
                if not valid_quotes:
                    print("Error: Incorrect quotation.")
                    return
                else:
                    args[start_idx] = args[start_idx].split('"')[1]
                    args[end_idx] = args[end_idx].split('"')[0]

                    # Join everything between the quotes into one argument.
                    temp = ' '.join(args[start_idx:end_idx + 1])

                    # Remove the elements we just joined together
                    # from the argument list.
                    for arg in args[start_idx:end_idx + 1]:
                        args.remove(arg)

                    # Insert the new, single string
                    # argument into the argument list.
                    args.insert(start_idx, temp)

            # Return unadulterated args if no
            # quotation found.
            return args
