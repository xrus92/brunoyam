x1 = float(input('Введите число 1: '))
x2 = float(input('Введите число 2: '))
max1 = (x1 > x2)*x1 + (x2 >= x1)*x2
print('Максимальное: ', max1)