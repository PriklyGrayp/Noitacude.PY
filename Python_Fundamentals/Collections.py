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
# 'how how to ind'

