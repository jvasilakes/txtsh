import os
import curses


ROOT = '/'
scr = curses.initscr()


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

	self.path = ROOT

	self.ls = os.listdir(self.path)

	self.num_listings = len(self.ls)

	self.curs = Cursor()

	self.curs.down_limit = self.num_listings + 2

	self.current_file = self.ls[self.curs.y - 4]


    def manage_input(self, direction):

	if direction == curses.KEY_UP:

	    if self.curs.y == self.curs.up_limit:
		return

	    else:
		self.curs.y -= 1

	elif direction == curses.KEY_DOWN:

	    if self.curs.y == self.curs.down_limit:
		return

	    else:
		self.curs.y += 1

	elif direction == curses.KEY_RIGHT:

	    self.build_path()

	    self.curs.y = 4

	elif direction == curses.KEY_LEFT:

	    self.shrink_path()

	    self.curs.y = 4

	else:
	    return


    def list_dir(self):

	self.ls = os.listdir(self.path)
	self.num_listings = len(self.ls)

	if self.num_listings == 0:

	    scr.addstr(4, 0, '*EMPTY*')

	else:

	    scr.addstr(2, 0, self.path)

	    for i in xrange(len(self.ls) - 1):

		scr.addstr(i + 4, 0, self.ls[i])

	    scr.refresh()


    def build_path(self):

	self.path = self.path + self.current_file + "/"

    
    def shrink_path(self):

	temp = self.path.split('/')

	temp.pop(len(temp) - 2)

	self.path = '/' + '/'.join([word for word in temp if word]) + '/'


    def navigate(self):

	c = None
	while c != ord('q'):

	    scr.clear()

	    scr.addstr(0, 0, "TXTSH FILE EXPLORER")

	    self.list_dir()

	    self.curs.display()

	    self.current_file = self.ls[self.curs.y - 4]

	    c = scr.getch()

	    self.manage_input(c)


	curses.endwin()


def main():

    curses.noecho()
    curses.curs_set(1)
    scr.keypad(1)


    expl = Explorer()

    path = expl.navigate()

    print path


if __name__ == '__main__':
    main()

