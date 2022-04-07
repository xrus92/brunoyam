x = int(input('Число 1: '))
y = int(input('Число 2: '))
z = int(input('Число 3: '))
if (x==y)&(y==z):
	print(3)
elif (x==y)|(x==z)|(y==z):
	print(2)
else:
	print(0)
