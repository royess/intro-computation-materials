# A solution to http://mathicpython.openjudge.cn/2020ex11/2/

def blur(n, m, pic):
    blurred_pic = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                blurred_pic[i][j] = pic[i][j]
            else:
                blurred_pic[i][j] = round(
                    (pic[i - 1][j]
                     + pic[i][j - 1] + pic[i][j] + pic[i][j + 1]
                     + pic[i + 1][j]) / 5)  # use round() to do the rounding
    return blurred_pic


n1, m1 = map(int, input().split(' '))
pic1 = []

for _ in range(n1):
    pic1.append(list(map(int, input().split(' '))))

blurred_pic1 = blur(n1, m1, pic1)

for i in range(n1):
    print(' '.join(map(str, blurred_pic1[i])))
