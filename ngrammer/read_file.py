from sys import argv

def read_file(text_file):
    '''
    # Opens and reads text_file. Returns
    # file contents as a string.
    '''

    with open(text_file, 'r') as f:
        file_string = f.read()

    return file_string
