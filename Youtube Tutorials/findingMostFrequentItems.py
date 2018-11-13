from collections import Counter

text = "Today I ate a chicken nugget and it was made out of chicken " \
       "and I also put some ketchup on it so that it would taste " \
       "so much better!"

words = text.split()
print(words)

count = Counter(words)
top_three = count.most_common(3)
print(top_three)

# Sort custom objects with different attributes
from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Bob', 'lname': 'Roberts'},
    {'fname': 'Bernie', 'lname': 'Sanders'},
    {'fname': 'Donald', 'lname': 'Trump'},
    {'fname': 'Amanda', 'lname': 'Hayes'},
    {'fname': 'Bernie', 'lname': 'Barbie'},
    {'fname': 'Tom', 'lname': 'Jones'},
    {'fname': 'Don', 'lname': 'Barbie'},
]

print('-----------------')

# Sorts alphabetically in first name then last name :)
for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)

# Sorting Custom Objects

from operator import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    "Like java toString()"
    def __repr__(self):
        return self.name + " : " + str(self.user_id)

users = [
    User('Jojo', 121),
    User('Sandy', 5),
    User('Brian', 69),
    User('Tuna', 18)
]

# Not sorted
for u in users:
    print(u)

print('______')

# Sorted by name
for user in sorted(users, key=attrgetter('name')):
    print(user)

print('______')

# Sorted by user_id
for user in sorted(users, key=attrgetter('user_id')):
    print(user)