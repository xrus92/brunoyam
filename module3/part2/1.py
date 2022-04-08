l = [1, 4, 1, 6, "hello", 1, 'a', 5, "hello", 6]
l2 = []
for i in range(len(l)):
	for j in range(i+1, len(l)):
		if (l[i] == l[j]) and (l2.count(l[j]) == 0):
			l2.append(l[j])
print(l, '\n',l2)