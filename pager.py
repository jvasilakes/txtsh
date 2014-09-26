import subprocess
import tempfile


def page(*args):

    tmp_file = open(tempfile.mkstemp()[1], 'w')

    tmp_file.write(*args)

    subprocess.call(['less', tmp_file.name])
