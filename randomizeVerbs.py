"""
randomizeVerbs.py

function: to randomize indexed values a specified list

author: Michelle Burroughs
"""


def randomizeVerbs(verb_num, verb_list_size):

    import random

    randomlist = []

    # populate random index list
    for i in range(verb_num):

        a = random.randint(0, verb_list_size-1)
        randomlist.append(a)

    print(randomlist)

    return randomlist


