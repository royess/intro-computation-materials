def judge_line(line):
    string = ''.join(line)
    return ('W'*5 in string), ('B'*5 in string)


def judge(chessboard):
    white_win, black_win = False, False

    # by row
    for i in range(15):
        line = chessboard[i]
        white_win_line, black_win_line = judge_line(line)
        white_win = white_win or white_win_line
        black_win = black_win or black_win_line

    # by col
    for j in range(15):
        line = [chessboard[i][j] for i in range(15)]
        white_win_line, black_win_line = judge_line(line)
        white_win = white_win or white_win_line
        black_win = black_win or black_win_line

    # by diag
    for i in range(15):
        line = [chessboard[i + k][k] for k in range(15 - i)]
        white_win_line, black_win_line = judge_line(line)
        white_win = white_win or white_win_line
        black_win = black_win or black_win_line

    for j in range(1, 15):
        line = [chessboard[k][j + k] for k in range(15 - j)]
        white_win_line, black_win_line = judge_line(line)
        white_win = white_win or white_win_line
        black_win = black_win or black_win_line

    # by back diag
    for i in range(15):
        line = [chessboard[i - k][k] for k in range(i + 1)]
        white_win_line, black_win_line = judge_line(line)
        white_win = white_win or white_win_line
        black_win = black_win or black_win_line

    for j in range(1, 15):
        line = [chessboard[14 - k][j + k] for k in range(15 - j)]
        white_win_line, black_win_line = judge_line(line)
        white_win = white_win or white_win_line
        black_win = black_win or black_win_line

    return white_win, black_win


num_case = int(input())

for _ in range(num_case):
    chessboard1 = [list(input()) for _ in range(15)]
    white_win1, black_win1 = judge(chessboard1)
    if white_win1 and black_win1:
        print('Both')
    elif white_win1:
        print('White')
    elif black_win1:
        print('Black')
    else:
        print('None')
