__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

f = open('wasteland.txt', mode='wt', encoding='utf-8')  # Write the text file
# help(f)

f.write('What are the roots that clutch', )
f.write('what branches grow\n')
f.write('Out of the stony rubbish? ')
f.close()
dir(f)

g = open('wasteland.txt', mode='rt', encoding='utf-8')  # Ready the text file
print(g.read(5))
print(g.read())
print(g.read(5))

g.seek(0)

print(g.readline())
print(g.readline())
print(g.readline())

g.seek(0)

print(g.readlines())

g.close()

h = open('wasteland.txt', mode='at', encoding='utf-8')  # Append to the end of the text file
h.writelines(['Son of man, \n',
             'You cannot say or guess, ',
             'for you know only, \n',
             'A heap of broken images, ',
             'where the sun beats\n'])
h.close()

i = open('wasteland.txt', mode='rt', encoding='utf-8')  # Ready the text file
print(i.read())
i.close()
