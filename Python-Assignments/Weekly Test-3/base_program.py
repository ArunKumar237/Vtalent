import sys
from random import seed, randrange

def generate_dictionary(x,y):
    try:
        # arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
        arg_for_seed, upper_bound = x,y
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()

    seed(arg_for_seed)
    mapping = {}
    for i in range(1, upper_bound):
        r = randrange(-upper_bound // 8, upper_bound)
        if r > 0:
            mapping[i] = r
    print('\nThe generated mapping is:')
    return mapping