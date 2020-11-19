def sort_num(n, reverse):
	digits = [(n//10**i)%10 for i in range(4)]
	return sum([ d*10**i for i, d in enumerate(sorted(digits, reverse=reverse))])

def one_step(n):
	n1 = sort_num(n, False)
	n2 = sort_num(n, True)
	n3 = n1 - n2
	print('{:04d} - {:04d} = {:04d}'.format(n1, n2, n3))
	return n3

n = int(input())

while n!=0 and n!=6174:
	n = one_step(n)
