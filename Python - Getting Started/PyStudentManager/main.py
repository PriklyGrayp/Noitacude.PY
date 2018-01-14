__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

import springfield_schools
SS = springfield_schools.Student()

class main():
    '''
    main.main()
    '''
    def __init__(self):
        '''Asking the user like to enter a student name'''
        string=False
        while string == False:
            userInput = input('Welcome to the Springfield Student hub. Would you like to add a student y/n: ')
            try:
                if userInput.isalpha() and userInput == 'y':
                    schoolName = self.user_school()
                    SS.read_file(schoolName)
                    name = self.user_name()
                    id = self.user_id()
                    SS.add_student(name, id)
                    SS.save_file(name, id, schoolName)
                    string=True
                elif userInput.isalpha() and userInput == 'n':
                    print('Good bye.')
                    string = True
                    pass
                else:
                    print(f'{userInput} is not a valid answer. Please respond with y/n.')

            except AttributeError:
                print(f'{userInput} is a number. Please respond with y/n.')


    def user_school(self):
        '''Asking the user which school'''
        string=False
        while string == False:
            school_type = input('Enter E for Elementary or H for High School. E/H: ')
            try:
                if school_type.isalpha() and school_type == 'E':
                    string = True
                    return'Springfield Elementary'
                elif school_type.isalpha() and school_type == 'H':
                    string = True
                    return 'Springfield High School'
                else:
                    print(f'{school_type} is not a valid answer. Please respond with E/H.')

            except AttributeError:
                print(f'{school_type} is a number. Please respond with E/H.')


    def user_name(self):
        '''Setting the student name by user input.'''
        string=False
        while string == False:
            student_name = input('Enter student name: ')
            try:
                if student_name.isalpha():
                    if self.compare_student_name(student_name):
                        print(f'Student name {student_name} already exists.')
                        continue
                    else:
                        print(f'Student name is {student_name}.')
                    string = True
                    return student_name
                else:
                    print(f'{student_name} is not a valid name.')

            except AttributeError:
                print(f'{student_name} is a number not a name.')


    def user_id(self):
        '''Setting the student ID by user input.'''
        string = False
        while string == False:
            student_id = input('Enter student ID: ')
            try:
                if self.compare_student_id(int(student_id)):
                    print(f'Student ID {student_id} already exists.')
                    continue
                else:
                    print(f'Student ID is {student_id}.')
                string = True
                return student_id

            except ValueError:
                print(f'{student_id} is made up of letters not an ID.')


    def compare_student_name(self, student_name):
        '''Checks to see if the name already exists'''
        for name in SS.get_students_titlecase():
            if student_name in name:
                return True
        return False


    def compare_student_id(self, student_id):
        '''Checks to see if the ID already exists'''
        for id in SS.get_students_id():
            if student_id == int(id):
                return True
        return False