import random
# import pickle

gryffindor = ['shimolee jhaveri', 'monica choi', 'imen graja', 'johanna kinsler',
    'georgiana ogrean', 'lucia racine']
hufflepuff = ['kimberly chuc', 'carolina de almedida e freitas', 'sarah fry', 
    'jessica huynh', 'janine martinez', 'jina zhu']
slytherin = ['amber chan', 'emily cheera', 'yichen dai', 'emily kuo', 'maggie ronan', 
    'sarah tao']
ravenclaw = ['elaine greer', 'lauren maghran', 'thuyvi nguyen', 'omoefe ogbeide',
    'nichole reyes', 'rowan shepherd']

all_houses = gryffindor + hufflepuff + slytherin + ravenclaw

def random_sort(students):
    random.shuffle(students)

    cutoff = len(students) // 2

    group1 = students[:cutoff]
    group2 = students[cutoff:]
    
    return tuple(zip(group1, group2))

def print_pairs(student_pairs):
    for first_student, second_student in student_pairs:
        print(f"{first_student.title()} and {second_student.title()}")

# House set 1
new_pairs = random_sort(gryffindor + hufflepuff) + random_sort(slytherin + ravenclaw)

# House set 2
#new_pairs = random_sort(gryffindor + ravenclaw) + random_sort(slytherin + hufflepuff)

# House set 3
#new_pairs = random_sort(gryffindor + slytherin) + random_sort(ravenclaw + hufflepuff)

# All houses
#print_pairs(random_sort(all_houses)) 


##Pickling for tracking: 
# past_pairs = pickle.loads(open(pickle_filename, "rb").read())

# for pair in new_pairs:
#     if past_pairs.has_key(pair):
#         # yell at me that they've already been paired
#     else:
#         # add current pair to past_pairs

# open(pickle_filename, "wb").write(pickle.dumps(past_pairs))

print_pairs(new_pairs)




