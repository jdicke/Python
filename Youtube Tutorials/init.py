class Tuna:

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Tuna(69)
jason.get_energy()

sandy = Tuna(96)
sandy.get_energy()

class Girl:
    gender = 'female'

    def __init__(self, name):
        self.name = name

r = Girl('Rachel')
s = Girl('Stanky')

print(r.gender)
print(r.name)
print(s.gender)
print(s.name)