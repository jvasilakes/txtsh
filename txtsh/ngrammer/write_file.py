def write_file(trigram_probs_dict, model_name=None):
    '''
    # Writes nicely formatted contents
    # of trigram_probs_dict to a file,
    # called trigram_model.txt. If the file
    # already exists, each new model is
    # appended to the end of the file.
    '''

    # Default model_name
    if not model_name:
        model_name = "UNTITLED MODEL"
    else:
        model_name = model_name.upper()

    # Open trigram_model.txt (create it if it doesn't exist)
    # in append mode.
    with open('trigram_model.txt', 'a') as f:

        # Write the model_name and column headers
        f.write(" \t\t**** {0} ****\n\n" .format(model_name))

        # Write the contents of the trigram model
        entries = 0
        for key, value in sorted(trigram_probs_dict.items()):
            f.write("  {0}  :  {1},  " .format(key, value))

            if entries == 5:
                f.write('\n')
                entries = 0
            else:
                entries += 1

        f.write('\n\n\n')

    return
