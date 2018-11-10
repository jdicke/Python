first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)

# Looks like [('Bucky', 'Roberts'), ('Tom', Hanks')]...

for a,b in names:
    print(a,b)