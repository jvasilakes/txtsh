#! /usr/bin/env python

import sys

import txtsh.log as log
from txtsh.shell import Shell


def main(argv):
    """
    The main driver function, which starts the shell.

    options:
        -v  verbose
    """
    log.start('.txtsh_log')
    log.write(mes="Txtsh started.")

    if argv[-1] == '-v':
        sh = Shell(verbose=True)
    else:
        sh = Shell()

    sh.run()

    return


if __name__ == '__main__':
    main(sys.argv)
