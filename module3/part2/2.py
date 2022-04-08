from random import randint
n = int(input('Введите размер матрицы: '))
mx = [[randint(0, 100) for i in range(n)] for j in range(n)]
print(mx)
max1 = 0
for i in mx:
    for j in i:
        if(max1 <= j):
            max1 = j
print('Максимальный элемент: ', max1)