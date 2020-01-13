import random
import pickle
import os.path
from os import path

#All of our 'houses'
gryffindor = ['shimolee', 'monica', 'imen', 'johanna', 'georgiana', 'lucia']
hufflepuff = ['kim', 'carolina', 'sarah fry', 'jessica', 'janine', 'jina']
slytherin = ['amber', 'emily cheera', 'yichen', 'emily kuo', 'maggie', 'sarah tao']
ravenclaw = ['elaine', 'lauren', 'vivi', 'omoefe', 'nichole', 'rowan']

all_houses = gryffindor + hufflepuff + slytherin + ravenclaw

def random_sort(students):
    random.shuffle(students)

    #Splits shuffled students into two sets, and defaults low if an odd number.
    cutoff = len(students) // 2

    group1 = students[:cutoff]
    group2 = students[cutoff:] 
    
    # Returns a tuple, of tuples, each with a student from each group.
    return tuple(zip(group1, group2))

def print_pairs(student_pairs):
    #Unpacks student_pairs tuple into first and second student to print.
    for first_student, second_student in student_pairs:
        print(f"{first_student.title()} and {second_student.title()}")



pickle_filename = 'past_pairs.pickle'


if path.exists(pickle_filename):
    # Check to see if pickle_filename already exists.
    # If so, open the file which returns a file object. 
    # Call .read on the file object returning a string of the file objects info.
    # Load the file info into past_pairs, using the pickle library. 
    # Otherwise, create an empty dictionary. 
    past_pairs = pickle.loads(open(pickle_filename, "rb").read())
else:
    past_pairs = {}

while True:

    # Create new pairs out of a selected 'house' set, and keep pairing until 
    # no duplicates are found. 
    # Change houses as needed. Currently set to: House set 1
    new_pairs = random_sort(gryffindor + hufflepuff) + random_sort(slytherin + ravenclaw)
    collisions = False
    
    # Check if new_pair is in past_pair, if collisions are found, break this for loop.
    for pair in new_pairs:
        if pair in past_pairs or tuple(reversed(pair)) in past_pairs:
            collisions = True
            break

    # If there are no collisions, break the while loop.
    if not collisions:
        break

# We can now add the unique pairs into past_pairs.
for pair in new_pairs:
    past_pairs[pair] = True

# Open the pickle_file in write mode (returns the file as an object). 
# Call .write on the file object and use the plckle library to dump/load the 
# updated (or new) pairs information into the file pickle_filename.
open(pickle_filename, "wb").write(pickle.dumps(past_pairs))

print_pairs(new_pairs)

# House set 1
# new_pairs = random_sort(gryffindor + hufflepuff) + random_sort(slytherin + ravenclaw)

# House set 2
# new_pairs = random_sort(gryffindor + ravenclaw) + random_sort(slytherin + hufflepuff)

# House set 3
# new_pairs = random_sort(gryffindor + slytherin) + random_sort(ravenclaw + hufflepuff)

# All houses
# new_pairs = random_sort(all_houses)


##Pickling for tracking: 
# past_pairs = pickle.loads(open(pickle_filename, "rb").read())

# for pair in new_pairs:
#     if past_pairs.has_key(pair):
#         # yell at me that they've already been paired
#     else:
#         # add current pair to past_pairs

# open(pickle_filename, "wb").write(pickle.dumps(past_pairs))




