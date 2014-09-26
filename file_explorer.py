import os
import curses


ROOT = '/'
HOMEDIR = '/home/jav/'

KEY_QUIT = ord('q')
KEY_CHOOSE_FILE = ord('c')

# -- Status codes ---
STOP = 0
GO = 1
CHOSEN = 2


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

    def __init__(self):

        self.scr = curses.initscr()

        curses.noecho()
        curses.curs_set(1)
        self.scr.keypad(1)

        self.path = HOMEDIR
        self.curs = Cursor()
        self.ls = os.listdir(self.path)
        self.num_listings = len(self.ls)
        self.curs.down_limit = self.num_listings + 3
        self.current_file = self.ls[self.curs.y - 4]

    def manage_input(self, key):

        if key == KEY_QUIT:
            return (STOP, None)

        elif key == KEY_CHOOSE_FILE:
            return (CHOSEN, self.path + self.current_file)

        elif key == curses.KEY_UP:

            if self.curs.y == self.curs.up_limit:
                pass

            else:
                self.curs.y -= 1

        elif key == curses.KEY_DOWN:
            if self.curs.y == self.curs.down_limit:
                pass
            else:
                self.curs.y += 1

        elif key == curses.KEY_RIGHT:
            self.build_path()
            self.curs.y = 4

        elif key == curses.KEY_LEFT:
            self.shrink_path()
            self.curs.y = 4

        else:
            pass

        return (GO, None)

    def list_dir(self):

        max_y = self.scr.getmaxyx()[0] - 5

        try:
            self.ls = os.listdir(self.path)

            for i in xrange(len(self.ls)):
                if self.ls[i].startswith('.'):
                    self.ls.pop(i)

        except:
            return

        self.num_listings = len(self.ls)

        if self.num_listings == 0:
            self.scr.addstr(4, 0, '*EMPTY*')

        else:

            self.scr.addstr(2, 0, self.path)

            for i in xrange(len(self.ls)):
                if i < max_y:
                    self.scr.addstr(i + 4, 0, self.ls[i])
                    self.scr.refresh()

            self.curs.down_limit = self.num_listings + 3

    def build_path(self):

        self.path = self.path + self.current_file + "/"

    def shrink_path(self):

        temp = self.path.split('/')
        temp.pop(len(temp) - 2)
        self.path = '/' + '/'.join([word for word in temp if word]) + '/'

    def navigate(self):

        status = GO

        c = None
        while status == GO:

            self.scr.clear()
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


if __name__ == '__main__':
    expl = Explorer()
    path = expl.navigate()
    if path:
        print path
