__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

students = []


def get_students_titlecase():
	students_titlecase = []
	for student in students:
		students_titlecase.append(student['name'].title())
	return students_titlecase


def print_students_titlecase():
	students_titlecase = get_students_titlecase()


def add_student(name, student_id=332):
	student = {'name': name, 'student_id': student_id }
	students.append(student)


def save_file(student):
	try:
		f = open('students.txt', 'a')
		f.write(student + '\n')
		f.close()
	except Exception:
		print('Could not save file.')


def read_file():
	try:
		f = open('students.txt', 'r')
		for student in f.readlines():
			add_student(student)
		f.close()
	except Exception:
		print('Could not read file.')


# string=False
# while string:
# 	userInput = input('Would you like to add a student: ')
# 	try:
# 		if userInput.isalpha():
# 			print(f'Student name is {userInput}.')
# 			string=True
# 		else:
# 			print(f'{userInput} is not a valid name.')

# 	except AttributeError:
# 		print(f'{userInput} is a number not a name.')


read_file()
print_students_titlecase()

student_name = input('Enter student name: ')
student_id = input('Enter student ID: ')

add_student(student_name, student_id)
save_file(student_name)