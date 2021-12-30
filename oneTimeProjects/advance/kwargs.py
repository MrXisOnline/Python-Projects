def add(**kwargs):
	print(kwargs)
	sum=0
	for item in kwargs.keys():
		sum += kwargs[item]
	return sum

print(add(a=1,b=2))
print(add(num1=2,num2=5,num3=6))