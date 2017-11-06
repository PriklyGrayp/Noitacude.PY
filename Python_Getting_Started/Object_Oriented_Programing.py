__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

'''Classes'''

students = []

class Student: # Parent Class

    school_name = 'Springfield Elementary' # Static var or Class attribute

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return 'Student ' + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

'''Inheritance and Polymorphism'''

class HightSchoolStudent(Student): # Derived Class

    school_name = 'Springfield High School'

    def get_school_name(self): # Overriding methods
        return 'This is a High School student'

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + '-HS'


james = HightSchoolStudent('james')
print(james.get_name_capitalize())