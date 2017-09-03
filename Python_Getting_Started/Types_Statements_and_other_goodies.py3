__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

'''
Numbers
'''
	'''
	Integers
	'''
	num = 45

	'''
	Floats
	'''
	pie = 3.14159

	'''
	Converting
	'''
	float(num)	== 45.0
	int(pie)	== 3


'''
Strings
'''
name = 'hi' or "hi" or'''hi''' or"""hi"""
number5 = '5' ornumber5 = str(5)

name.capitalize() 		== 'Hi'
name.relace('i', 'ey') 	== 'hey'
name.isalpha() 			== True # True this string made up of letters.
number5.isdigit() 		== True # True this string made up of numbers.

	'''
	String Format Function
	'''
	name = 'PythonBo'
	machine = 'HAL'

	'Nice to meet you {0}. I am {1}'.format(name, machine)
	or
	f'Nice to meet you {name}. I am {machine}'

	'C:\\users\\documents'
	r'C:\\users\documents' # raw
	u'C:\\users\documents' # unicode


'''
Bools and None
'''
A = True
B = False #
int(A) == 1
int(B) == 0
str(A) =='True'

foo = None # Null, placeholder, False

'''
If Statements
'''
number = 5
if number ==5:
	print('Number is 5.')
else: print('Number is not 5.')

if A: # if A is True/dose exsist
	print('This will execute')

if foo: # if foo is True/dose exsist
	print('This will not execute')

'''
Ternary statements
'''
'bigger' if num > pie else 'smaler'



'''
Lists
'''
student_names = []
student_names = ['Mark', 'Katerina', 'Jessica']
student_names[0] == 'Mark' # Lists start at 0
student_names[-1] == 'Jessica' # Lists ends at -1
student_names.append('Homer') # Adds to the list
'Mark' in student_names == True 
len(student_names) == 4 # Number of elements in the list
del student_names[2] # Jessica is no longer i nthe list

student_names = ['Mark', 'Katerina', 'Jessica']
student_names[1:] == ['Katerina', 'Jessica']
student_names[1:-1] == ['Katerina']


'''
Loops
'''
	'''
	For loops
	'''
	student_names = ['Mark', 'Katerina', 'Jessica']
	for name in student_names:
		print(f'Student name is {name}')

	'''
	Break and Continue
	'''
	student_names = ['James', 'Katerina', 'Jessica', 'Mark', 'Bort', 'Frank Grimes']
	for name in student_names:
		if name == 'Bort':
			continue
			print(f'Found {name}')
		print(f'Currently testing {name}.')

	'''
	While loops
	'''
	count = 0
	while count < len(student_names):
		print(f'Student name is {student_names[count]}')
		count += 1

	range(5, 10, 2) # Starts at 5
					# Ends at 9
					# incriments by 2


'''
Dictionaries
Lets you store Key and Value pairs.
'''
student = {
	'name' : 'mark'
	'student_id' : 15163
	'feedback' : None
}

all_students = [
	{'name' : 'Mark', 'student_id' : 15163},
	{'name' : 'Katerina', 'student_id' : 63112},
	{'name' : 'Jessica', 'student_id' : 30021}	
]

student['name'] == 'Mark'
student['last_name'] == KeyError # Wont work because it does not exsist
student.get('last_name', 'Unknown') == 'Unknown' # If it does not exsist then returs your second value
student.keys() == ['name', 'student_id', 'feedback']
student.values() == ['Mark', 15163, None]
student['name'] = 'James' # Wil lreplace Mark with James
del student['name'] #This will remove the key value pair


'''
Exceptions
When to use it: Dealing with user input
'''
student = {
	'name' : 'mark'
	'student_id' : 15163
	'feedback' : None
}

student['last_name'] = 'Kowalski'

try:
	last_name = student['last_name'] # Wont work because it does not exsist
	numbered_last_name = 3 + last_name
except KeyError as error:
	print('Error finding last name')
	print(error)
except TypeError as error:
	print('I cant add these together')
	print(error)
except Exception as error:
	print('Unknown error')
	print(error)

print('This code executes!')


'''
Other data types
'''
complex
long # Python 2 only replaced by int
bytes and bytearray # A sequence of intigers in a range of 0 - 255.
tuple = (3, 5, 1, 'Mark') # Imutable cannot change their values
set and frozenset #removes duplicates and reorders the lsit
set([3, 2, 3, 1, 5]) == (1, 2, 3, 5)