def fmax(*args):
	maxi = args[0]

	for j in args:
		if str == type(j):
			raise Exception("Input Only Numbers!!!")

	for i in args:
		if i > maxi:
			maxi = i

	return maxi

print(fmax(3,9,8,1))
