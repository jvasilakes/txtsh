import re


def preprocess_line(file_string):
    '''
    # Reads in file string returned by read_file()
    # and removes all characters that are not
    # whitespace, [a-z][A-Z], comma, or period.
    # Changes all characters to lowercase and
    # converts numerals to 0.
    '''

    # Convert to lowercase.
    processed_string = file_string.lower()

    # Delete any characters that are not a digit,
    # whitespace, a-z, comma, or period.
    processed_string = re.sub(r'[^\d\sa-z,.]', r'', processed_string)

    # Convert all digits to 0.
    processed_string = re.sub(r'\d', r'0', processed_string)

    # Replace all whitespace with single space.
    processed_string = re.sub(r'\s', r' ', processed_string)

    return processed_string
