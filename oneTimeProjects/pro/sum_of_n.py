n = int(input("Terms :"))

sum_n=0
for i in range(1,n):
	if i%2==0:
		sum_n -= 1/(i*2)
	else:
		sum_n += 1/(i*2)
print(f"sum : {round(sum_n,2)}")