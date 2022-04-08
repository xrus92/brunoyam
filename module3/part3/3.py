def maxnumber(numbers):
	import itertools
	temp = list(itertools.permutations(numbers, len(numbers)))
	comb = []
	for i in temp:
		tempstr = ''
		for j in i:
			tempstr += str(j)
		comb.append(int(tempstr))
	return print(max(comb))

l1 = [56, 9, 11, 2]
l2 = [3, 81, 5]
l3 = [1, 700, 10, 1000, 5, 7]
l4 = [100, 10, 1]
maxnumber(l1)
maxnumber(l2)
maxnumber(l3)
maxnumber(l4)