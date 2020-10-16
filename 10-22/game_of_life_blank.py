import copy

# update the universe
def update(univ):
    # please complete this function, note that this function should MODIFY the parameter univ
    return

# print the universe in a compact format
def show(univ):
    for row in univ:
        for term in row:
            print(term, end='')
        print()

if __name__=='__main__':
    # initial state: spaceship
    univ = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    for t in range(21):
        print('Round', t, '\n')
        show(univ)
        update(univ)
        print('\n------\n')
