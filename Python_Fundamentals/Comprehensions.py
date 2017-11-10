__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

'''List'''

words = 'Why sometimes I do these things that I do sometimes.'.split()
print(words)

print([len(word) for word in words])

'''Set'''
print({len(word) for word in words})

'''Dictionary'''
from pprint import pprint as pp

country_to_capital = {'UK':'London',
                       'SA':'Cape Town',
                       'S':'Stockholm'}
print(country_to_capital)

capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)