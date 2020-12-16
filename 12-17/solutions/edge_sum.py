# A solution to http://mathicpython.openjudge.cn/2020ex11/1/

def get_edge_sum(m, n, mat):
    return sum([mat[i][j] for i in range(m) for j in range(n)
                if i == 0 or i == m - 1 or j == 0 or j == n - 1])


m1, n1 = map(int, input().split(' '))
mat1 = []

for _ in range(m1):
    mat1.append(list(map(int, input().split(' '))))

print(get_edge_sum(m1, n1, mat1))
