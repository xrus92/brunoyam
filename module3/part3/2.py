def len5(s):
	s2 = s.split()
	delim = ['[','\n',',','.','|','/',']','(','{','-','_','=','+','?','}',')']
	words = []
	for i in s2:
		if (i not in delim) and (len(i) < 5):
			words.append(i)
	return words


s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того...
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

print(len5(s))