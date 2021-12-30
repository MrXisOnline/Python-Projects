def get_rev_sum(num):
	s = str(num)
	rev = s[::-1]
	sum = 0
	for d in rev:
		sum = sum + int(d)
	print(f"Reverse :{rev}")
	print(f"Sum of degits : {sum}")

get_rev_sum(359)