from random import randint


class Animal:
    _DEGREE_OF_DANGER = 0
    live = True
    sound = None

    def __init__(self, speed: int):
        self._cords, self.speed = [0, 0, 0], speed

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords = [dx*self.speed, dy*self.speed, dz*self.speed]

    def get_cords(self):
        print('X: %d, Y: %d, Z: %d' %
              (self._cords[0], self._cords[1], self._cords[2]))

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound != None:
            print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz)*self.speed/2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = 'Click-click-click'

    def __init__(self, speed):
        super().__init__(speed)


# для проверки:
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
