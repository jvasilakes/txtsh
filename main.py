#! /usr/bin/python2

import log

from shell import Shell


def main():

        log.write("Txtsh started.")

        sh = Shell()
        sh.run()

        return


if __name__ == '__main__':
        main()
