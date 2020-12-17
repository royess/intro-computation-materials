def get_div_num(total_num, max_num):
    if total_num == 0:
        return 1
    if total_num < 0:
        return 0
    if max_num == 0:
        return 0
    return get_div_num(total_num - max_num, max_num) + get_div_num(total_num, max_num - 1)


n = int(input())
print(get_div_num(n, n))
