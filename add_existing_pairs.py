import random, os.path, pickle
from os import path
from pair_maker import print_pairs, pickle_filename

existing_pairs = (("carolina","amber"))

if __name__ == '__main__':
    if path.exists(pickle_filename):
        # Check to see if pickle_filename already exists.
        # If so, open the file which returns a file object. 
        # Call .read on the file object returning a string of the file objects info.
        # Load the file info into past_pairs, using the pickle library. 
        # Otherwise, create an empty dictionary. 
        past_pairs = pickle.loads(open(pickle_filename, "rb").read())
    else:
        past_pairs = {}

    for pair in existing_pairs:
        past_pairs[pair] = True

    # Open the pickle_file in write mode (returns the file as an object). 
    # Call .write on the file object and use the plckle library to dump/load the 
    # updated (or new) pairs information into the file pickle_filename.
    open(pickle_filename, "wb").write(pickle.dumps(past_pairs))