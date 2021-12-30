import random
import numpy as np

# # generate a random float b/w 0-1 excluded
# print(random.random())

# # if we need a number think of a simple random from 0-100
# print(int(random.random()*100)) # we can do it

# # randint used to generate random no. from range
# print(random.randint(10,25)) # both no. also included

# # randrange also do same as randint but both no. excluded
# print(random.randrange(10,25))

# # used in statistics
# # it generate random number b/w mean & standard deviation
# a = random.normalvariate(0, 1)
# print(a)

# # get a random element from list
# mylist = [1,2,3,4,5,6]
# print(random.choice(mylist))

# # get multiple random element from list
# print(random.sample(mylist, 2))

# # randomly shuffle list
# random.shuffle(mylist)
# print(mylist)


# random.seed(1)
# print(random.random())
# random.seed(1)
# print(random.random())

# create array of 3 element with random float
print(np.random.rand(3))

# create array of 3 by 3 with random float
print(np.random.rand(3,3))

# create array of 3 by 3 with random int first two arg. are range
print(np.random.randint(0,10,(3,3)))
