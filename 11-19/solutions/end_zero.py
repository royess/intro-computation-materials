def get_num_end_zeros(n):
    s = 0
    while n!=0:
        n //= 5
        s += n
    return s

N = int(input())
inputs = [ int(input()) for _ in range(N) ]

for n in inputs:
    print(get_num_end_zeros(n))
