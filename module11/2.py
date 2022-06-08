import unittest
from peewee import *

db = SqliteDatabase('sqlite2.db')

class Students(Model):
	id = PrimaryKeyField()
	name = CharField()
	surname = CharField()
	age = IntegerField()
	city = CharField()

	class Meta:
		database = db

class Courses(Model):
	id = PrimaryKeyField()
	name = CharField()
	time_start = CharField()
	time_end = CharField()

	class Meta:
		database = db

class StudentCourses(Model):
	student_id = ForeignKeyField(Students)
	courses_id = ForeignKeyField(Courses)

	class Meta:
		database = db
		indexes = ((('student_id','courses_id'), True),)

def create_tables():
	Students.create_table()
	Courses.create_table()
	StudentCourses.create_table()

def data_fill():
	courses_data = [(1, 'python', '21.07.21', '21.08.21'),(2, 'java', '13.07.21', '16.08.21')]
	students_data = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
				(3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
	student_courses_data = [(1, 1), (2, 1), (3, 1), (4, 2)]
	try:
		Courses.insert_many(courses_data, fields=[Courses.id, Courses.name, Courses.time_start, Courses.time_end]).execute()
	except IntegrityError:
		print('table filling skipped...')
	try:
		Students.insert_many(students_data, fields=[Students.id, Students.name, Students.surname, Students.age, Students.city]).execute()
	except IntegrityError:
		print('table filling skipped...')
	try:	
		StudentCourses.insert_many(student_courses_data, fields=[StudentCourses.student_id, StudentCourses.courses_id]).execute()
	except IntegrityError:
		print('table filling skipped...')

def get_students_older_than(age):
	return Students.select().where(Students.age > age)
	
def get_students_oncourse(course):
	return Students.select().join(StudentCourses).join(Courses).where(Courses.name == course)

def get_students_oncourse_from(course, city):
	return Students.select().join(StudentCourses).join(Courses).where(Courses.name == course, Students.city == city)

def add_student(id, name, surname, age, city):
	try:
		Students.insert(id = id, name = name, surname = surname, age = age, city = city).execute()
		return True
	except:
		return False

def add_course(id, name, time_start, time_end):
	try:
		Courses.insert(id = id, name = name, time_start = time_start, time_end = time_end).execute()
		return True
	except:
		return False

def delete_student(id):
	try:
		StudentCourses.delete().where(StudentCourses.student_id == id).execute()
		Students.delete().where(Students.id == id).execute()
		return True
	except:
		return False

def add_student_course(student_id, courses_id):
	try:
		StudentCourses.insert(student_id = student_id, courses_id = courses_id).execute()
		return True
	except:
		return False

class TestDB(unittest.TestCase):

	# def test_add_student(self):
	# 	self.assertTrue(add_student(5, 'Vasya','Petrov', 21, 'Spb'))

	def test_add_student1(self):
		self.assertFalse(add_student(5, 'Vasya','Petrov', 21, 'Spb'))

	def test_delete_student(self):
		self.assertTrue(delete_student(5))

	# def test_add_course(self):
	# 	self.assertTrue(add_course(3, 'css','13.07.21', '16.08.21'))

	# def test_add_student_course(self):
	# 	self.assertTrue(add_student_course(5,3))

create_tables()
data_fill()
# age = 30
# print(f'Students older than {age}:')
# for i in get_students_older_than(30):
# 	print(i.name, i.surname)

# course = 'python'
# print(f'\nStudents on course \'{course}\':')
# for i in get_students_oncourse(course):
# 	print(i.name, i.surname)

# city = 'Spb'
# print(f'\nStudents on course \'{course}\' and from \'{city}\':')
# for i in get_students_oncourse_from(course, city):
# 	print(i.name, i.surname)

if __name__ == '__main__':
	unittest.main()