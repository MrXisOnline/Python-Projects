from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat

# # product	(It make the product of iterables with each other)
# a = [1,2]
# b = [3,4]
# prod = product(a,b) 	# returns an iterables
# print(list(prod))

# # permutations
# a = [1,2,3]
# perm = permutations(a)
# print(list(perm))

# # combinations
# a = [1,2,3,4]
# comb = combinations(a, 2)	# give combination and second arg. is length
# print(list(comb))

# # accumulate

# a = [1,2,3,4]
# acc = accumulate(a) # it adds the list by element
# print(a)
# print(list(acc))

# # groupby

# def sml_3(x):
# 	return x < 3

# a = [1,2,3,4]
# grp = groupby(a, key=sml_3) # used to group elements by function
# for key, value in grp:
# 	print(key, list(value))

# infinite iterables

# # count
# for i in count(10):		# it creates an inf. loop start from 10
# 	print(i)
# 	if i == 11:
# 		break

# # cycle
# x = 1
# a = [1,2,3]
# for i in cycle(a):		# create inf. loop by list
# 	print(i)
# 	x+=1
# 	if x == 5:
# 		break

# # repeat
# x = 1
# for i in repeat(1):			# create inf. loop and repeat 1 alltime
# 	print(i)
# 	x += 1
# 	if x == 4:
# 		break