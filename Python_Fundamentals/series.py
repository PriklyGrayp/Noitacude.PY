__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

'''Read and print an integer series.'''

import sys

def read_series(filename):
    with  open(filename, mode='rt', encoding='utf-8') as f:
        return [ int(line.strip()) for line in f]

def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == '__main__':
    main('recaman.dat')
    # main(sys.argv[1])