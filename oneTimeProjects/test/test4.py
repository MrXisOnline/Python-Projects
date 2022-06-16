i=0
j=72
ar = []

while True:
    if j < 0:
        break
    ar.append((i, j, i*j))
    i=i+4
    j=j-4
print(ar)