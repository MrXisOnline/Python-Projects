from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# # Counter

# a = "aaaaaaaabbbcc"
# my_count = Counter(a) 	# Counts the element inside a string returns dict
# print(my_count)

# # namedtuple

# point = namedtuple("point", "x,y") # it is like a structure to make tuple
# pt = point(1,-4)	# but with names or a struct in C
# print(pt)
# print(pt.x, pt.y)

# # OrderedDict (it is a dictionary which remembers the order)
# # but in python 3.6 normal dict also remember order of element as inserted
# orderdict = OrderedDict()
# orderdict["a"] = 2
# orderdict["c"] = 5
# orderdict["f"] = 6
# print(orderdict)

# # defaultdict (it have the default value of a key with is doesnt have)
# defdict = defaultdict(int)
# defdict["a"] = 3
# defdict["b"] = 5
# print(defdict)
# print(defdict["c"])

# deque (it is a list but it can do operation on both sides)
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.rotate(2)	# rotate all elements by two indies
print(d)