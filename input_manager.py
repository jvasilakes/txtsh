import inspect

from importlib import import_module

from header import *


class InputManager(object):

    def __init__(self, shell):

        self.shell = shell

        # Container for cached imports from self.import_cmd_set
        self.cmd_set_cache = {}

    def _exec(self, input, data_object=None):

        if not input:
            return GO

        input = input.strip().lower()

        cmd_set = self.import_cmd_set()

        if not self.is_command(input, cmd_set):
            return GO

        args = self.findArgs(input)

        if data_object is not None:
            args.insert(1, data_object)

        if len(args) == 1:
            status = cmd_set.map[args[0]]()

        elif len(args) > 1:
            status = cmd_set.map[args[0]](*args[1:])

        else:
            status = GO

        return status

    def import_cmd_set(self):

        sh_type = self.shell.getType

        # Python does this for us!
        # Use cached import if available
        # if sh_type in self.cmd_set_cache:
        #    return self.cmd_set_cache[sh_type]

        #else:

        if sh_type == 'Shell':
            cmds = import_module('command_shell')

        elif sh_type == 'Subshell':
            cmds = import_module('command_subshell')

        else:
            print "Error: Invalid shell!"
            return

        self.cmd_set_cache.update({sh_type: cmds})

        return cmds

    def is_command(self, input, commands):

        args = input.split(None, 1)

        if args[0].startswith('!'):
            if args[0] in commands.map.keys():
                return True
            else:
                print "'{}' is not a valid command." .format(args[0])
                return False

        else:
            return False

    def findArgs(self, input):

        args = input.split()

        if len(args) == 1:
            return args

        else:

            quote_found = False

            for arg in args:

                if arg.startswith('"'):

                    quote_found = True
                    valid_quotes = False
                    start_idx = args.index(arg)

                    for arg in args[start_idx:]:

                        if arg.endswith('"'):
                            valid_quotes = True
                            end_idx = args.index(arg)

                            break

            # Return with error if valid quotation was not used.
            if quote_found:

                if not valid_quotes:

                    print "Error: Incorrect quotation."
                    return

                else:

                    # Remove quotation.
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

            else:
                # Just return args
                pass

            return args
