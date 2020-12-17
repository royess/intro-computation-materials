s = input()
s = s[:s.find('*') + 1]
counts = [0, 0, 0, 0]

for c in s:
    if '0' <= c <= '9':
        counts[0] += 1
    elif 'a' <= c <= 'z':
        counts[1] += 1
    elif 'A' <= c <= 'Z':
        counts[2] += 1
    else:
        counts[3] += 1

for n in counts:
    print(n)
