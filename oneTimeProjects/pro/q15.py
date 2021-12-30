def check_duplicates(lst):
	occ = {}
	for d in lst:
		if d in occ.keys():
			occ[d] = occ[d] + 1
		else:
			occ[d] = 1
	for k in occ.keys():
		if occ[k] > 1:
			print(occ)
			return True
	return False

print(check_duplicates([1,2,3,4,5,6,6]))