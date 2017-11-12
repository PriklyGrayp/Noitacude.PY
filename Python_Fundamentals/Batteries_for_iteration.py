__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

from itertools import islice, count
from Predicates import is_prime
from Lucas import lucas

# islice(all_primes, 1000)

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(thousand_primes)
print(sum(islice((x for x in count() if is_prime(x)), 1000)))

print(any(is_prime(x) for x in range(1328, 1361)))

print(all(name == name.title() for name in ['South Africa', 'London', 'Sydney']))

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 23, 21, 19, 17]
tuesday = [13, 14, 14, 14, 16, 20, 21, 22, 23, 21, 19, 17]

for temps in zip(sunday, monday, tuesday):
    print('min={:4.1f}, max={:4.1f}, average={:4.1f}'.format(min(temps), max(temps), sum(temps) / len(temps)))

temperatures = chain(sunday, monday, tuesday)
print(all(t > 0 for t in temperatures))

for x in (p for p in lucas() if is_prime(p)):
    print(x)