from functools import reduce
# func = lambda x,y: x+y
# print(func(5,1))
print(list(map(lambda x: x*2, [i for i in range(1,5)])))			# map all element again by function
print(list(filter(lambda x: x%2==0, [i for i in range(1,5)])))	# filter elements by function
print(reduce(lambda x,y: x*y, [i for i in range(1,5)]))	# reduce th element by function
