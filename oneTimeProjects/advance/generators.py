import sys
import time

# # this is how generator created
# def generator():
# 	yield 1
# 	yield 2
# 	yield 3

# s = generator()
# by next function we get to next yield value
# print(next(s))
# print(next(s))
# print(next(s))
# after last next function if we call again we get error

# # getting sum of all yeild
# print(sum(s))

# # this function return a list 
# def firstn(n):
# 	nums = []
# 	for i in range(n):
# 		nums.append(i)
# 	return nums

# def firstn_generator(n):
# 	for i in range(n):
# 		yield i

# start = time.time()
# print(sys.getsizeof(firstn(1000000)))
# print("function time", time.time() - start)
# start = time.time()
# print(sys.getsizeof(firstn_generator(1000000)))
# print("generator time", time.time() - start)

a = (i for i in range(100000))
print(next(a))
print(next(a))
print(next(a))