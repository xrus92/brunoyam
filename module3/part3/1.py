def area(a, b, c):
	p = (a + b + c) / 2
	return (p*(p-a)*(p-b)*(p-c))**0.5
a = float(input('Сторона a = '))
b = float(input('Сторона b = '))
c = float(input('Сторона c = '))
print('Площадь треугольника =', area(a,b,c), 'кв. см')