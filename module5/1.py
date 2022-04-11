class StringVar:
	def __init__(self, text):
		self.text = text

	def get(self):
		return self.text
		
	def set(self, text):
		self.text = text

s = StringVar(input('Введите строку: '))
print(s.get())
s.set('Строка изменилась')
print(s.get())