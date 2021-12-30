def check_prime(num):
	f = 0
	if num == 1:
		return True
	for i in range(2,num):
		if num%i==0:
			f += 1
			break
	if f != 0:
		print("Not a Prime")
		return False
	else:
		print("It\'s a Prime")
		return True

check_prime(17)