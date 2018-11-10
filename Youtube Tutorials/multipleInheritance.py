class Mario():

    def moving(self):
        print("I am moving")

class Shroom():

    def eat_shroom(self):
        print("Now I am big")

class Fire():

    def shoot_fire(self):
        print("Now I am shooting fire")

class BigMario(Mario, Shroom, Fire):
    pass

bm = BigMario()
bm.moving()
bm.eat_shroom()
bm.shoot_fire()
