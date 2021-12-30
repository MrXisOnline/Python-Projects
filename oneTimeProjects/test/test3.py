
rows = 9
for i in range(rows):
	for j in range(rows): 
		if i != 0 and i != rows-1:
			if j == 0 or j == rows-1:
				print("*", end="")
			else:
				print(" ", end="")
		else:
			print("*", end="")
	print()