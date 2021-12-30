# recursive execution example
def recur(a):
	print(a)
	return recur(a+1)

recur(0)