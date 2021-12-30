def add(*args):
	sum=0
	for item in args:
		sum += item
	return sum

print(add(1,2,4))
print(add(5,8,2,4,7))