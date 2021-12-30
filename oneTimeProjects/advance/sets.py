# a = {1,2,3,4,4}
# b = {0,4,6,2}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

a = {1,2,3,4,4}
b = {1,2,3}
c = {5,6,7}

print(a.issubset(b))
print(b.issubset(a))
print(a.issuperset(b))
print(a.isdisjoint(b)) #if both have no intersection