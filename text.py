import sys
import re

import log


class Text(object):

    members = []

    def __init__(self):

        self.filepath = None
        self.id = self.set_id()
        self.title = ''
        self.contents = ''
        self.words = {}
        self.numbers = {}
        self.punctuation = {}
        self.members.append(self)

    def set_id(self):

        if self.members:
            return (self.members[(len(self.members) - 1)].id) + 1
        else:
            return 1

    def load_data(self, data_type, data):

        if data_type.lower() == 'file':
            data = self.readfile(data)

            if not data:
                log.write("Could not read from {}" .format(self.filepath))
                print "Could not read from {}" .format(self.filepath)
                return

        # Get rid of unwanted newlines in the title.
        self.title = re.sub(r'\s+', ' ', data[:20])
        # Save the unadulterated data.
        self.contents = data
        # Tokenize the data, separating contractions such as "I'm"
        # into "I" and "'m", and separating punctuation.
        temp = re.findall(r'[^\'\w+\s+]|\'?\w+', data)

        for item in temp:

            # If there's an alphabetic character, it's probably a word.
            if re.search(r'[a-zA-Z]', item):
                l = self.words
            elif item.isdigit():
                l = self.numbers
            else:
                l = self.punctuation

            if item in l:
                l[item] += 1
            else:
                l.update({item: 1})

        print "Data loaded into id {}." .format(self.id)

    def readfile(self, data):

        self.filepath = data

        try:
            with open(data, 'r') as f:
                data = f.read()
                return data

        except:
            return None
