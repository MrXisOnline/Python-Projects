def duplicate(num, string):
	return [str(string)*x for x in range(1,num+1)]


def alter_elements(tup1,tup2):
	try:
		if len(tup1) != len(tup2):
			raise IndexError
		res_l=[]
		for i in range(len(tup1)):
			res_l.append((tup1[i],tup2[i]))
	except IndexError:
		print("Give Only Tuples Of Same Length")
	else:
		return tuple(res_l)


def compute_elements(lst):
	comp = {}
	for e in lst:
		if type(e) == str:
			continue
		elif type(e) == list:
			for i in e:
				if i in comp.keys():
					comp[i] = comp[i] + 1
				else:
					comp[i] = 1
		else:
			if e in comp.keys():
				comp[e] = comp[e] + 1
			else:
				comp[e] = 1
	return comp
