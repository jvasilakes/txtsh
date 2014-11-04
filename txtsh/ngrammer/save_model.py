from __future__ import print_function

import os
import errno
import ast


# TODO: Change this to use pickle/dill
def save_model(trigram_probs_dict, model_name=None):
    '''
    # Write trigram_probs_dict to file with
    # name model_name and extension '.mod'.
    '''
    model_dir = 'models/'
    try:
        os.makedirs(model_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    if not model_name:
        model_name = "unknown_model.mod"
    else:
        model_name = model_name + ".mod"

    if os.path.isfile(model_dir + model_name):
        print("Overwriting exisiting model '{0}'..." .format(model_name))

    with open(model_dir + model_name, 'w') as f:
        f.write(str(trigram_probs_dict))

    print("Model written to '{0}'." .format(model_dir + model_name))


def open_model(file_name, model_dir='models/'):
    '''
    # Attempts to open file_name in model_dir and
    # read it in as a python dict.
    '''

    s = open(model_dir + file_name, 'r').read()
    model_dict = ast.literal_eval(s)

    if not isinstance(model_dict, dict):
        print("'{0}' does not appear to be a dict." .format(file_name))
        return

    return model_dict
