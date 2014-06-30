#! /usr/bin/python2

from header import *
from command import _info
from shell import Shell


def main():

	_info()	

	sh = Shell()
	sh.run()

	return


if __name__ == '__main__':
	main()

