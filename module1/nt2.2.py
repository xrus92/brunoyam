x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
if (x1==x2):
	if (abs(y1-y2) < 8):
		print('YES')
elif (y1==y2):
	if (abs(x1-x2) < 8):
		print('YES')
else:
	print('NO')
