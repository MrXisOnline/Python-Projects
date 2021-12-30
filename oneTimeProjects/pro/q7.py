def get_gcd(num1,num2):
	mul1 = []
	mul2 = []
	cd = []
	if num1 < num2:
		for d in range(2,num2+1):
			if num1%d==0:
				mul1.append(d)

			if num2%d==0:
				mul2.append(d)
	else:
		for d in range(2,num1+1):
			if num1%d==0:
				mul1.append(d)

			if num2%d==0:
				mul2.append(d)

	for e in mul1:
		if e in mul2:
			cd.append(e)
	if len(cd) != 0:
		return max(cd)
	else:
		return 1

def get_lcm(num1,num2):
	gcd = get_gcd(num1,num2)
	lcm = (num1*num2)/gcd
	print(f"LCM : {int(lcm)}")

get_lcm(5,45)