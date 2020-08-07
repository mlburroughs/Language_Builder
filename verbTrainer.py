"""

Verb trainer: Function to randomize verb list into a flash card function.

Author: Michelle Burroughs

"""


def verbTrainer(verb_list):

    import random

    # Welcome to User
    print("Bienvenue a Verb S'entrainer, there are " + str(len(verb_list)) + " verbs in the system.")
    print("Type exit or stop to discontinue")
    print()

    # User inputs numbers of verbs to test
    verb_num = input('Please enter desired number of verbs to test: ')

    print()
    # stop exercise control
    if verb_num == 'exit' or verb_num == 'stop':
        print("Exercise stopped")
        return
    else:
        verb_num = int(verb_num)
        print('You will complete ' + str(verb_num) + " exercises")

    # initialized parameters
    correct_response = 0
    verb_list_size = len(verb_list)
    randomlist = []
    response_array = []

    # populate random index list
    for i in range(verb_num):

        a = random.randint(0,verb_list_size-1)
        randomlist.append(a)

    print(randomlist)

    # populate test list
    for vowel in randomlist:

        test_keys = verb_list.keys()
        keys = list(test_keys)
        test_verb = keys[vowel]
        print(test_verb)
        print('Quel verb est-il en anglais? ' + str(test_verb))
        response = input()
        test_values = verb_list.values()
        values = list(test_values)

        test_answer = values[vowel]
        if response == test_answer:
            correct_response += 1
            print('Correct!')
        elif response == 'exit' or response == 'stop':
            print('exercise stopped')
            return
        else:
            print('Incorrect...')
            print()
            response_array.append(test_verb)

    grade = (correct_response/verb_num) * 100
    print('All set. Your score is ' + str(grade) + " percent. Tout a l'heure")

    return grade

