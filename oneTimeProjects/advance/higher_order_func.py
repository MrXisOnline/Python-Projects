def add(n1, n2):
	return n1 + n2

def sub(n1, n2):
	return n1 - n2

def mul(n1, n2):
	return n1 * n2

def div(n1, n2):
	return n1 / n2

def calc(n1, n2, func):		# calc is higher order function
	return func(n1, n2)		# can take functions as input

print(calc(4, 8, mul))