# bisection.py

# A program that estimates the square root of a number between 1 and 100 using the bisection method

import numpy as np

def root(num):
	a = 0.1
	b = 10.1
	for i in range(20):
		p = (a + b) / 2
		f_a = num - a**2
		f_p = num - p**2
		print (p)
		if f_a * f_p < 0:
			a = a
			b = p
		else:
			a = p
			b = b


num = float(input("Enter number: "))
root(num)

