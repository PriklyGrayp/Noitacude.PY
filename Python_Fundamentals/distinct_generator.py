__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

import take_generator as tg

def distinct(iterable):
    '''Return unique items by eliminating duplicates.

    Args:
        iterable: The source series.

    Yields:
        Unique elements in order from'iterable'.
    '''
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)

def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in tg.take(3, distinct(items)):
        print(item)

if __name__ == '__main__':
    run_pipeline()