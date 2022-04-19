import sqlite3

def create_tables():
	connection = sqlite3.connect('sqlite1.db')
	cursor = connection.cursor()
	try:
		cursor.execute('''CREATE TABLE Students (
						id INTEGER PRIMARY KEY,
						name Varchar(32),
						surname Varchar(32),
						age INTEGER,
						city Varchar(32));''')
	except sqlite3.Error:
		pass
	try:
		cursor.execute('''CREATE TABLE Courses (
						id INTEGER PRIMARY KEY,
						name Varchar(32),
						time_start timestamp,
						time_end timestamp);''')
	except sqlite3.Error:
		pass
	try:
		cursor.execute('''CREATE TABLE Student_courses (
						student_id INTEGER, course_id INTEGER, FOREIGN KEY (course_id) REFERENCES Courses (id),
						FOREIGN KEY (student_id) REFERENCES Students (id));''')
	except sqlite3.Error:
		pass
	connection.close()


def data_fill():
	connection = sqlite3.connect('sqlite1.db')
	cursor = connection.cursor()
	courses_data = [(1, 'python', '21.07.21', '21.08.21'),(2, 'java', '13.07.21', '16.08.21')]
	students_data = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
				(3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
	student_courses_data = [(1, 1), (2, 1), (3, 1), (4, 2)]
	try:
		cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", students_data)
		cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", courses_data)
		cursor.executemany("INSERT INTO Student_courses VALUES (?, ?)", student_courses_data)
		connection.commit()
	except sqlite3.Error:
		pass
	connection.close()

def get_students_older_than(age):
	connection = sqlite3.connect('sqlite1.db')
	cursor = connection.cursor()
	cursor.execute("SELECT name, surname FROM Students WHERE age > " + str(age))
	result = cursor.fetchall()
	connection.close()
	return result

def get_students_oncourse(course):
	connection = sqlite3.connect('sqlite1.db')
	cursor = connection.cursor()
	cursor.execute('''SELECT Students.name, Students.surname FROM Students, Courses, Student_courses WHERE 
					Students.id = Student_courses.student_id AND Courses.id = Student_courses.course_id AND
					courses.name = \'''' + course +'\'')
	result = cursor.fetchall()
	connection.close()
	return result

def get_students_oncourse_from(course, city):
	connection = sqlite3.connect('sqlite1.db')
	cursor = connection.cursor()
	cursor.execute('''SELECT Students.name, Students.surname FROM Students, Courses, Student_courses WHERE 
					Students.id = Student_courses.student_id AND Courses.id = Student_courses.course_id AND
					courses.name = \'''' + course +'\' AND Students.city = \''+ city + '\'')
	result = cursor.fetchall()
	connection.close()
	return result

create_tables()
data_fill()
age = 30
print(f'Students older than {age}:')
for i in get_students_older_than(30):
	print(i[0], i[1])

course = 'python'
print(f'\nStudents on course \'{course}\':')
for i in get_students_oncourse(course):
	print(i[0], i[1])

city = 'Spb'
print(f'\nStudents on course \'{course}\' and from \'{city}\':')
for i in get_students_oncourse_from(course, city):
	print(i[0], i[1])