firstName = 'string'
print(firstName)
players = [69, 1, 42, 66, 97, 21]
print("My players:", players[:])

age = 27

if age < 21:
    print("No beer for you!")
else:
    print("Enjoy your beer!")

print()
name = "Lucy"

if name is "Bucky":
    print("Hey there Bucky")
elif name is "Lucy":
    print("What up Lucedawg?")
else:
    print("Please sign up for the site!")

#######
##Left off on episode: 16
#######

foods = ["bacon", "tuna", "ham", "snausages", "beef"]

for f in foods[:2]:
    print(f)
    print(len(f))

print()

for x in range(10, 40, 5):
    print(x)

print()
buttcrack = 5

while buttcrack < 10:
    print(buttcrack)
    buttcrack += 1

'''
This program finds a magic number.
It uses a for loop and break
'''

magicNumber = 26;

for n in range(101):
    if n is magicNumber:
        print("Magic number is ", n)
        break
    else:
        print(n)

'''
This program prints out every number that is divisible by 4
'''

for n in range(101):
    if n % 4 is 0:
        print(n)

numbersTaken = [2,5,12,13,17]

print("Here are the numbers that are still available")

for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)

#Whenever it gets to continue whatever is after skip it and go back to the iteration of the loop

'''
Functions
'''

def beef():
    print("Dayum, functions are cool!")

def bitcoin_to_usd(btc):
    amount = btc * 527
    print("$", amount)

beef()
bitcoin_to_usd(4)
bitcoin_to_usd(5.27)
bitcoin_to_usd(13.5)

def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

bucky_limit = allowed_dating_age(19)
creepy_bob_limit = allowed_dating_age(49)

print("Bucky can date girls", bucky_limit, "or older")
print("Creepy Bob can date girls", creepy_bob_limit, "or older")

def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()