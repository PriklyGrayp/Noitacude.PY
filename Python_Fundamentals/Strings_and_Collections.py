__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"


'''Strings'''
a = 'first' 'second'
print(a)

b = '''This is
a multi line
string'''
print(b)

c = '''This is\na multi line\nstring'''
print(c)

d = 'This is a \" in a string'
print(d)

e = 'This is a \\ in a string'
print(e)

path = r'C:\Users\***\Documents'  # The r in the front make this string raw
print(path)


'''Bytes'''
d = b'some bytes'  # The b in the front make this sa bytes data type

norsk = ''

data = norsk.encode('utf-8')
norwegian = data.decode('utf-8')


'''While'''
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)