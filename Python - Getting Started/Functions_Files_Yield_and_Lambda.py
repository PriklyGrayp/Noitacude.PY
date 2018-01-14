__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

'''
Functions
'''
def doThings():
	things = 'Things are done.'
	print(things)
	return things


'''
Arguments
'''
def doThings(what = 'Things'):
	things = f'Doing {what}.'
	print(things)
	return things

doThings('work')


def var_args(name, *args): # *Args becomes a list
	print(name)
	print(args)


def var_kwargs(name, **kwargs): # **kwargs becomes a dictionary
	print(name)
	print(kwargs)

var_kwargs('Mark', description='loves PY3', feedback=None)

'''
Yield
'''
students = []


def read_file():
	try:
		f = open('students.txt', 'r')
		for student in read_students(f):
			students.append(student)
		f.close()
	except Exception:
		print('Could not read file.')


def read_students(f):
	for line in f:
		yield line


read_file()
print(students)


'''
Lambda Functions
'''
def double(x):
	return x * 2

or

double = lambda x: x * 2