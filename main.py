#! /usr/bin/env python

import txtsh.log as log
from txtsh.shell import Shell


def main():
    """
    The main driver function, which starts the shell.
    """
    log.start('.txtsh_log')
    log.write(mes="Txtsh started.")

    sh = Shell()
    sh.run()

    return


if __name__ == '__main__':
        main()
