import sys
import log

try:
    from nltk import word_tokenize
    log.write("nltk successfully imported.")

except Exception as e:
    log.write(e, error=True)
    raise e


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

        if data_type == 'file':
            self.filepath = data

            try:
                with open(data, 'r') as f:
                    data = f.read()

            except:
                print "Could not read from file: {}." .format(data)
                return GO

        self.title = data[:20]
        self.contents = data
        temp = word_tokenize(data)

        for item in temp:

            if item[0].isalpha():
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
