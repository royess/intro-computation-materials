s1 = input()
s2 = input()

s1, s2 = s2[:2]+s1[2:], s1[:2]+s2[2:]

print(s1)
print(s2)
