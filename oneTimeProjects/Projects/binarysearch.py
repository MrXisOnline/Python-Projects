
def binary_search(l,n):
	low = 0
	high = len(l) - 1
	mid = 0

	while low <= high:
		mid = (high+low)//2

		if l[mid] < n:
			low = mid + 1
		elif l[mid] > n:
			high = mid - 1
		else:
			return mid
	return -1


print(binary_search(list(range(23,2300,2)), 1087))


