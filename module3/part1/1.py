x = float(input('Сумма вклада: '))
p = float(input('Процентная ставка: '))
y = float(input('Желаемая сумма: '))
years = 0
while x < y:
	x += int(x * (p / 100))
	years += 1
print('Через', years, 'лет вы накопите', y, 'или больше рублей')