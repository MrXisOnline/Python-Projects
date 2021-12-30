def seq1():
	for i in range(1,5):
		for j in range(i,0,-1):
			print(j, end=" ")
		print()

def seq2():
	r = 6
	c = r
	for i in range(r):
		for j in range(c-1):
			print(" ", end="")
		c -= 1
		for k in range(1,i):
			print(k,end="")
		for l in range(i-2,0,-1):
			print(l,end="")
		print()
	c=r
	for m in range(r-1):
		for o in range(0,m+1):
			print(" ",end="")
		for n in range(1,c-2):
			print(n,end="")
		c -= 1
		for p in range(c-3,0,-1):
			print(p,end="")
		print()

seq1()
print("\n"*3)
seq2()