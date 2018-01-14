__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

import springfield_schools
SS = springfield_schools.Student()

class Students():
    '''
    main.main()
    '''
    def __init__(self, school_name, student_name, student_id):
        schoolName = self.user_school(school_name)
        SS.read_file(schoolName)
        name = self.user_name(student_name)
        id = self.user_id(student_id)
        SS.add_student(name, id)
        SS.save_file(name, id, schoolName)



    def user_school(self, school_name):
        '''Asking the user which school'''
        string=False
        while string == False:
            try:
                if school_name.isalpha() and school_name == 'E':
                    string = True
                    return'Springfield Elementary'
                elif school_name.isalpha() and school_name == 'H':
                    string = True
                    return 'Springfield High School'
                else:
                    print(f'{school_name} is not a valid answer. Please respond with E/H.')

            except AttributeError:
                print(f'{school_name} is a number. Please respond with E/H.')


    def user_name(self, student_name):
        '''Setting the student name by user input.'''
        string=False
        while string == False:
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


    def user_id(self, student_id):
        '''Setting the student ID by user input.'''
        string = False
        while string == False:
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