from __future__ import print_function

import txtsh.log as log

from txtsh.header import *
from txtsh.input_manager import InputManager


class Shell(object):
    """
    The main txtsh shell.
    Implemented as a singleton.
    """

    members = []

    def __init__(self, verbose=False):

        self.PROMPT = 'TXTSH> '
        self.input_manager = InputManager(self, verbose)

        # Starting values.
        self.state = GO
        self.cmd = None

        # If this is the first shell spawned upon
        # starting the program, show the user some
        # exciting information.
        if not self.members:
            self.input_manager.manage('!info')

        self.addToMembers()

    @property
    def Type(self):
        """
        Return the shell's type as a string.
        Used within InputManager.import_cmd_set()
        """
        temp = str(type(self))
        return temp.rsplit('.')[-1][:-2]

    def addToMembers(self):
        if isinstance(self, Subshell):
            self.members.append(self)
        else:
            if not self.members:
                self.members.append(self)

    def run(self):
        """
        The driver for the shell.
        """
        try:
            while self.state == GO:
                print(self.PROMPT, end="")
                self.cmd = raw_input()
                self.state = self.input_manager.manage(self.cmd)

            while self.state == STOP:
                print("Thx 4 using txtsh!!!")
                break

        # Ctrl+C
        except KeyboardInterrupt:
            ans = raw_input(" Quit txtsh? [y/n]: ")
            ans.lower() != 'y' and self.run()
            return

        # Ctrl+D
        except EOFError:
            print("\r")
            self.run()

        except Exception as e:
            log.write(mes=str(e), traceback=True)
            print("ERROR: {}" .format(e))
            self.run()


class Subshell(Shell):
    """
    Created when user types "!use <ID>".
    Kept distinct from the main shell
    to avoid confusion.
    """

    def __init__(self, data_object):

        Shell.__init__(self)

        if not data_object:
            print("No data_object specified.")
        else:
            self.data = data_object

        self.PROMPT = 'ID: {}> ' .format(self.data.id_num)

    def run(self):
        while self.state == GO:
            print(self.PROMPT, end="")
            self.cmd = raw_input()
            self.state = self.input_manager.manage(self.cmd,
                                                  data_object=self.data)
        del self
