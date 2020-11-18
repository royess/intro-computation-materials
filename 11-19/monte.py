import math
import random

def f(x):
	return (x**2 + x + math.exp(x)) / (x**3 - x + 1)

def monte_integ(x, num_samples):
	y_upper_lmt = 6.0
	integ = 0
	for _ in range(num_samples):
		u = x * random.random()
		y = y_upper_lmt  * random.random()
		if y<f(u):
			integ += 1
	integ *= x*y_upper_lmt/num_samples
	return integ

num_inputs = int(input())
inputs = []

for _ in range(num_inputs):
	inputs.append(float(input()))

num_samples = 1000000

for x in inputs:
	print('{:.1f}'.format(monte_integ(x, num_samples)))
