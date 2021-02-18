import random

def create_outline():
    """
    TODO: implement your code here
    """

    top = { # This defines and declares the topics SET
        'Introduction to Python',
        'Tools of the Trade',
        'How to make decisions',
        'How to repeat code',
        'How to structure data',
        'Functions',
        'Modules'
    }
    top = list(top) # Cast the topics SET to a LIST
    top.sort() # Sort the topics LIST alphabetically

    print('Course Topics:')
    for i in top: # for items in topics
        print('*',i) # print items

    prob = [ # This defines and declares the problems LIST
        'Problem 1',
        'Problem 2',
        'Problem 3'
    ]
    print('Problems:')
    for i in top:
        top_dict = {i:prob} # i is items; prob is values in topics_dictionary
        for k,v in top_dict.items(): # for keys and values in topics_dictionary
            print('*', k, ':', ', '.join(map(str,v)))

    s_names = ( # This defines and declares the student_names TUPLE
        'Alpha',
        'Bravo',
        'Charlie'
    )
    prog = ( # This defines and declares the progress TUPLE
        'STARTED',
        'GRADED',
        'COMPLETED'
    )
    posi_n = 0 # This defines the student position number on the list
    prog_c = 0 # This defines the student progress counter

    print('Student Progress:')
    while posi_n < len(s_names):
        r = random.randint(0,2) # Generates a random integer for indexing
        # This define and declares the grade TUPLE for the student position starting from 1,
        # the random student name, the random topic, the random problem
        # and the student progress starting from 0
        grade = (str(posi_n+1) + '.', s_names[r], ' - ', top[r], ' - ', prob[r], f'[{prog[prog_c]}]')
        print(*grade) # This unpacks the grade TUPLE using an asterisk; no sep='' (seperator) is defined
        posi_n += 1
        prog_c += 1

    pass

    # keys = ()
    # problems = (['Problem 1','Problem 2','Problem 3'],)
    # topics = {'Introduction to Python','Introduction to Python','Tools of the Trade','How to make decisions','How to repeat code','How to structure data','Functions','Modules'}
    # dictionary = {}

    # print('Course Topics:')
    # for value in topics:
    #     keys = topics
    #     print("* " + value)
    
    # print(keys)
    # print('Problems:')
 
    # for item in keys:
    #     dictionary = dict(zip(keys,problems))
    #     # print(dictionary)
    #     # print('%s %s' % (item,dictionary))

    # print(dictionary)

if __name__ == "__main__":
    create_outline()
