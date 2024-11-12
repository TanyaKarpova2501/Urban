class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self,_cords, speed):
        self._cords = _cords
        _cords = [0, 0, 0]
        self.speed = speed

    def move(self,dx, dy, dz):
        new_x = self._cords + dx * self.speed
        new_y = self._cords + dy * self.speed
        new_z = self._cords + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cards(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    def __init__(self):
        baek = True

    def lay_eggs(self):
        print("Here are(is) <случайное число от 1 до 4> eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def diva_in(self, dz):
        dz = dz // 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Animal, Bird, AquaticAnimal, PoisonousAnimal):
    super().live()
    super().beak()

    super().speack()
    super().attack()

    super().move()
    super().get_cards()
    super().diva_in()
    super().lay_eggs()
    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

