def fibonacci(num, a=0, b=1):
	if a < num:
		print(a, end=" ")
		c = a
		a = b
		b = b + c
		fibonacci(num, a, b)

fibonacci(30)
