def digits_sum(n):
	s = 0
	while n!=0:
		s += n%10
		n //= 10
	return s

def k_min_beau(k):
	i = 1
	n = 1
	while i<=k:
		if digits_sum(n)==10:
			i += 1
		n += 9
	n -= 9
	return n

k = int(input())
print(k_min_beau(k))