import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self,dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        num_ = random.randint(1,4)
        print(f"Here are(is) {num_} eggs for you")

class AquaticAnimal(Animal):
    def __init__(self,speed):
        super().__init__(speed)
        _DERGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * self.speed / 2


class PoisonousAnimal(Animal):
    def __init__(self,speed):
        super().__init__(speed)
        _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)
        sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

#db.speed()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()