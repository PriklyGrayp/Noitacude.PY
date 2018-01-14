__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

def take(count, iterable):
    '''Take items from the front of an iterable.
    
    Args:
        count: The maximum number of items to retrive.
        iterable: The source series.
        
    Yields:
        At most 'count' items from 'iterable'
    '''
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)

if __name__ == '__main__':
    run_take()