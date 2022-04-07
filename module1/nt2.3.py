password = ''
difficult = 0
while ((len(password) < 8) + (not(difficult)) > 0):
	password = str(input('Введите пароль: '))
	p_l, p_u, difficult = 0, 0, 0
	for symbol in password:
		if(symbol.islower()):
			p_l = 1
		if(symbol.isupper()):
			p_u = 1
	if p_l & p_u:
		difficult = 1
else:
	print('Пароль достаточно сложный')