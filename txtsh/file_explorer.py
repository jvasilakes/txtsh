from __future__ import print_function

import os
import sys
import curses

import txtsh.log as log


class Cursor(object):

    def __init__(self):

        self.y = 4
        self.x = 0
        self.up_limit = 4
        self.down_limit = 4

    def display(self):
        curses.setsyx(self.y, self.x)
        curses.doupdate()


class Explorer(object):
    """
    A curses-based file explorer. 
    Returns the path of a file selected.
    """

    def __init__(self):

        # Status codes
        self.STOP = 0
        self.GO = 1
        self.CHOSEN = 2

        # Directory aliases
        self.ROOTDIR = '/'
        self.HOMEDIR = os.path.expanduser("~")

        # Key aliases
        self.KEY_QUIT = ord('q')
        self.KEY_CHOOSE_FILE = ord('c')
        self.KEY_UP = [curses.KEY_UP, ord('k')]
        self.KEY_DOWN = [curses.KEY_DOWN, ord('j')]
        self.KEY_LEFT = [curses.KEY_LEFT, ord('h')]
        self.KEY_RIGHT = [curses.KEY_RIGHT, ord('l')]

        # Create a cursor
        self.curs = Cursor()
        # Start the screen
        self.create_scr()

        self.path = self.HOMEDIR + '/'
        self.ls = os.listdir(self.path)
        self.num_listings = len(self.ls)
        self.curs.down_limit = self.num_listings + 3
        self.current_file = self.ls[self.curs.y - 4]

    def create_scr(self):
        """
        Start the curses screen.
        """
        self.scr = curses.initscr()
        curses.noecho()
        curses.curs_set(1)
        self.scr.keypad(1)

    def navigate(self):
        """
        The driver function for the file explorer.
        Returns the path of a selected file to the txtsh shell.
        """
        status = self.GO

        c = None
        while status == self.GO:

            self.scr.erase()
            self.scr.addstr(0, 0, "TXTSH FILE EXPLORER")
            self.scr.addstr(1, 0, "'c' to choose file, \
                                  'q' to quit without choosing.")

            self.list_dir()
            self.curs.display()
            self.current_file = self.ls[self.curs.y - 4]

            c = self.scr.getch()
            (status, path) = self.manage_input(c)

        curses.endwin()

        return path

    def manage_input(self, key):
        """
        Return status and file path if CHOSEN
        to Explorer.navigate(). status is one of GO, STOP, or CHOSEN
        """
        status = self.GO
        path = None

        if key == self.KEY_QUIT:
            status = self.STOP
            path = None

        elif key == self.KEY_CHOOSE_FILE:
            status = self.CHOSEN
            path = self.path + '/' + self.current_file

        elif key in self.KEY_UP:
            if self.curs.y == self.curs.up_limit:
                pass
            else:
                self.curs.y -= 1

        elif key in self.KEY_DOWN:
            if self.curs.y == self.curs.down_limit:
                pass
            else:
                self.curs.y += 1

        elif key in self.KEY_RIGHT:
            self.build_path()
            self.curs.y = 4

        elif key in self.KEY_LEFT:
            self.shrink_path()
            self.curs.y = 4

        else:
            pass

        return (status, path)

    def list_dir(self):
        """
        List the contents of the current directory
        in the explorer screen.
        """
        max_y = self.scr.getmaxyx()[0] - 5

        # Get the current directory listing.
        try:
            self.ls = os.listdir(self.path)
            # Filter the directory listing to not include hidden files.
            self.ls = filter(lambda f: not f.startswith('.'), self.ls)
            self.num_listings = len(self.ls)

        except Exception:
            log.write(traceback=True)
            return

        # Display the directory listing.
        if self.num_listings == 0:
            self.scr.addstr(4, 0, '*EMPTY*')
        else:
            self.scr.addstr(2, 0, self.path)
            for i in xrange(len(self.ls)):
                if i < max_y:
                    self.scr.addstr(i + 4, 0, self.ls[i])
                    self.scr.noutrefresh()
            self.curs.down_limit = self.num_listings + 3

    def build_path(self):
        self.path = os.path.join(self.path, self.current_file)

    def shrink_path(self):
        self.path = os.path.abspath(os.path.join(self.path, '..'))


if __name__ == '__main__':
    expl = Explorer()
    path = expl.navigate()
    if path:
        print(path)
