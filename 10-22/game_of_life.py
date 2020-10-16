import copy

def update(univ):
    univ1 = copy.deepcopy(univ) # copy the old univ
    numrow = len(univ)
    numcol = len(univ)

    for row in range(numrow):
        for col in range(numcol):
            urow = (row-1) % numrow
            drow = (row+1) % numrow
            lcol = (col-1) % numcol
            rcol = (col+1) % numcol

            numnb = sum([
                univ1[urow][lcol],  univ1[urow][col],   univ1[urow][rcol],
                univ1[row][lcol],                       univ1[row][rcol],
                univ1[drow][lcol],  univ1[drow][col],   univ1[drow][rcol]
            ])

            if univ1[row][col]==0 and numnb==3:
                univ[row][col] = 1
            elif univ1[row][col]==1 and not numnb in [2,3]:
                univ[row][col] = 0

def show(univ):
    for row in univ:
        for term in row:
            print(term, end='')
        print()

if __name__=='__main__':
    univ = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    for t in range(10):
        print('Round', t, '\n')
        update(univ)
        show(univ)
        print('\n------\n')
