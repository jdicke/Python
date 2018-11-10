class Parent():

    def print_last_name(self):
        print('Roberts')

class Child(Parent):

    def print_first_name(self):
        print('Bobby')

    def print_last_name(self):
        print('Snitzleberg')

me = Child()
me.print_first_name()
me.print_last_name()