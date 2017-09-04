__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

class HightSchoolStudent(Student):  # Derived Class

    school_name = 'Springfield High School'

    def get_school_name(self):  # Overriding methods
        return 'This is a High School student'

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + '-HS'