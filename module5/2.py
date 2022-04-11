class Point:
	def __init__(self, x, y):
		self.x, self.y = x, y

	def __str__(self):
		return f"{self.x},{self.y}"

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def distance(self, other):
		return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

p1 = Point(10, 20)
p2 = Point(5, 10)

print(p1 + p2)
print(p1 - p2)
print(p1.distance(p2))