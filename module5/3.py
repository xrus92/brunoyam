from random import randint
class Warrior:

	def __init__(self, health, end, armor):
		self.health = health
		self.end = end
		self.armor = armor

	def __str__(self):
		return f"(HP{self.health} | A{self.armor} | E{self.end})"

	def attack(self):
		if self.end > 0:
			self.end -= 10
		if self.end < 0:
			self.end = 0	
		if self.health < 0:
			self.health = 0	

	def attack2(self):
		self.health -= randint(10,30)
		self.end -= 10
		if self.end < 0:
			self.end = 0
		if self.health < 0:
			self.health = 0

	def defend(self, other):
		if self.health > 10:
			if self.armor > 0:
				self.armor -= randint(0,10)
				if other.end > 0: 
					self.health -= randint(0,20)
				else:
					self.health -= randint(0,10)				
				if self.armor < 0:
					self.armor = 0
			else:
				self.armor = 0
				self.health -= randint(10,30)
		if self.health < 0:
			self.health = 0	

w1 = Warrior(100, 100, 100)
w2 = Warrior(100, 100, 100)

while(w1.health > 10 and w2.health > 10):
	r = randint(1,4)
	print(w1,"vs",w2)
	if r == 1:
		print('<<<<Атаковал первый воин>>>>')
		w1.attack()
		w2.defend(w1)
	elif r == 2:
		print('<<<<Атаковал второй воин>>>>')
		w2.attack()
		w1.defend(w2)
	elif r == 3:
		print('<<<<Атаковали вместе>>>>')
		w1.attack2()
		w2.attack2()
	else:
		print('<<<<Оба защищаются>>>>')
print(w1,"vs",w2)
if w1.health > w2.health:
	print('Победил первый воин!')
	defeat = w2
elif w1.health < w2.health:
	print('Победил второй воин!')
	defeat = w1
elif w1.health == w2.health and w2.health !=0:
	print('Ничья!')
	exit()
else:
	print('Оба погибли!')
	exit()
print("Pollice verso? (да, нет): ",end='')
if(input() == 'да'):
#	defeat.health = 0
	print(defeat,'мертв :(')
else:
	print('Бой окончен')