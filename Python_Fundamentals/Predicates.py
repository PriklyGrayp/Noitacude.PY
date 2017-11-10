__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

from math import sqrt
from pprint import pprint as pp

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print([x for x in range(101) if is_prime(x)])

prime_square_divisors = {x*x:(1, x, x*x) for x in range(101) if is_prime(x)}

pp(prime_square_divisors)