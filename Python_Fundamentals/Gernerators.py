__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

'''Specift iterable sequences
are lazy evaluated
can model infinite sequences
are composable into pipelines
'''

def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
print(g)
print(next(g))
print(next(g))
print(next(g))

for v in gen123():
    print(v)

def gen246():
    print('About to yield 2')
    yield 2
    print('About to yield 4')
    yield 4
    print('About to yield 6')
    yield 6
    print('About to return')

G = gen246()
print(next(G))
print(next(G))
print(next(G))
print(next(G))