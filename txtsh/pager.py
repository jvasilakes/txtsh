import subprocess
import tempfile
import os


def page(args):
    """
    Run the argument through 'less'.
    """
    if os.path.isfile(args):
        subprocess.call(['less', args])

    else:
        tmp_file = open(tempfile.mkstemp()[1], 'w')
        tmp_file.write(args)
        subprocess.call(['less', tmp_file.name])
