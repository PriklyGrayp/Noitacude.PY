__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

# print('executing __main__.py with name {}'.format()__name__)

import sys

import reader

r = reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()
