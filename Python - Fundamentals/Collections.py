'''Tuple'''
t = ('Norway', 4.953, 3)
t + (12322, 'Hello')
t * 3

a = ((1245,555), (785568,'Tuples'))
a[0]
a[0][0]

h = (157,)  # Always trail with a comma

(a, (b, (c, d))) = (1, (8, (10, 5)))

# a == 1
# b == 8
# c == 10
# d == 5

a = 14
a, b = b, a


'''String'''
a = len('Cape town')
# a == 9

a = 'Cape' + 'Town'

# a == 'CapeTown'

a = '_'.join(['Cape', 'Town'])
# a == 'Cape_Town'

a = 'CapeTown'.partition('peTo')
# a == ('Ca', 'peTo', 'wn')

a = 'Ca{0} To{1}'.format('pe', 'wn')
# a == 'Cape Town'


'''Range'''
a = range(5)
# a == (0, 5)
for b in a:
    print(b)
# 0
# 1
# 2
# 3
# 4

a = list(range(0, 10, 2))
# 0 = starting value.
# 10 = stop value.
# 2 = step value
# a == [0, 2, 4, 6, 8]

a = [1, 58, 648, 6545]
for b in enumerate(a):
    print(b)
# (0, 1)
# (1, 58)
# (2, 648
# (3, 6545)


'''List'''
a = 'show how to index'

a[1:-2]


'''Set'''
p = set()
p.(5, 8, 9)

blue_eyes ={'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

blue_eyes.union(blond_hair)
blue_eyes.intersection(blond_hair)
blue_eyes.difference(blond_hair)
blue_eyes.symmetric_difference(blond_hair)
smell_hcn.issubset(blond_hair)
smell_ptc.issuperset(smell_hcn)
a_blood.isdisjoint(o_blood)