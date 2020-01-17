import pickle, os.path, sys
from os import path
from pair_maker import print_pairs, pickle_filename

if path.exists(pickle_filename):
    # Check to see if pickle_filename already exists.
    # If so, open the file which returns a file object. 
    # Call .read on the file object returning a string of the file objects info.
    # Load the file info into past_pairs, using the pickle library, 
    # then print past_pairs. 
    # Otherwise, exit immediately with an error. 
    past_pairs = pickle.loads(open(pickle_filename, "rb").read())
    print_pairs(past_pairs)
else:
    sys.exit(f"Couldn't load {pickle_filename}!")