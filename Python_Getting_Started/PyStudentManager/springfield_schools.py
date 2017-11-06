__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

students = []

class Student():


	def get_students_titlecase(self):
		students_titlecase = []
		for student in students:
			students_titlecase.append(student['name'].title())
		return students_titlecase


	def get_students_id(self):
		students_id = []
		for id in students:
			students_id.append(id['student_id'])
		return students_id


	def add_student(self, name, student_id):
		student = {'name': name, 'student_id': student_id}
		students.append(student)


	def save_file(self, name, student_id, school_name):
		try:
			print(f'{school_name}.txt')
			f = open(f'{school_name}.txt', 'a')
			f.write(name + ':' + student_id + '\n')
			f.close()
		except Exception:
			print('Could not save file.')


	def read_file(self, school_name):
		try:
			f = open(f'{school_name}.txt', 'r')
			for student in f.readlines():
				line = student.split(':')
				name = line[0]
				id = line[1].strip()
				self.add_student(name, int(id))
			f.close()
		except Exception:
			print('Could not read file.')