__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

from contextlib import closing

class RefrigeratorRaider:
    '''Raid a refrigerator'''

    def open(self):
        print('Open fridge door.')

    def take(self, food):
        print('Finding {}...'.format(food))
        if food == 'deep fried pizza':
            raise RuntimeError('Health warning!')
        print('Taking {}'.format(food))

    def close(self):
        print('Close fridg door.')

def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)

raid('bacon')
raid('deep fried pizza')