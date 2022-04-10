def insertion_sort(m):
    for i in range(1, len(m)):
        temp = m[i]
        j = i - 1
        while (j >= 0 and temp < m[j]):
            m[j + 1] = m[j]
            j = j - 1
        m[j + 1] = temp
    return m 
       
def binary_search(m, e):
    if len(m) < 2:
        if e == int(m[0]):
            print('Элемент найден в позиции 0')
        else:
            print('Элемент не найден!')
    else:
        start, end = 0, len(m)
        while start <= end:
            mid = (start + end) // 2
            if m[mid] == e:
               return print('Элемент найден в позиции', mid)
            elif m[mid] < e:
                start = mid + 1
            else:
                end = mid - 1
        return print('Элемент не найден!')
m = input('Введите массив чисел через пробел: ').split()
m = [int(x) for x in m]
print('Отсортированный массив: ', end='')
m = insertion_sort(m)
print(m)
e = int(input('Введите элемент для поиска: '))
binary_search(m , e)