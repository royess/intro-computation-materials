# A solution to http://mathicpython.openjudge.cn/2020ex11/5/

def get_code(word):
    code = ''
    for c in word:
        if c == ' ':
            val = 0
        else:
            val = ord(c) - ord('A') + 1
        code += '{:0>5}'.format(bin(val)[2:])
    return code


def rotate_clockwise(dx, dy):
    return dy, -dx


def fill_code(num_rows, num_cols, code):
    code += '0' * (num_rows * num_cols - len(code))
    mat = [[-1 for _ in range(num_cols)] for _ in range(num_rows)]
    x, y = 0, 0
    dx, dy = 0, 1

    for bit in code:
        mat[x][y] = bit
        if x + dx == -1 or x + dx == num_rows or y + dy == -1 or y + dy == num_cols \
                or mat[x + dx][y + dy] != -1:
            dx, dy = rotate_clockwise(dx, dy)
        x += dx
        y += dy

    return mat


num_rows1, num_cols1, word1 = input().split(' ', 2)
num_rows1 = int(num_rows1)
num_cols1 = int(num_cols1)
code1 = get_code(word1)
mat1 = fill_code(num_rows1, num_cols1, code1)

for i in range(num_rows1):
    print(''.join(mat1[i]), end='')
