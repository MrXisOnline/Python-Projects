def sum_of_odd_even(n):
	sum_odd = 0
	sum_even = 0
	for d in range(1,n+1):
		if d%2==0:
			sum_even += d
		else:
			sum_odd += d
	print(f"Sum of Odd :{sum_odd}")
	print(f"Sum of Even :{sum_even}")
	return (sum_odd,sum_even)

sum_of_odd_even(10)