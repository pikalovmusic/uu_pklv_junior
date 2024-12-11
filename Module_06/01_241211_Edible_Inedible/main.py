class Animal:
    def __init__(self, name):
        self.name, self.alive, self.fed = name, True, False

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел "{food.name.lower()}"')
            self.fed = True
            return

        print(f'{self.name} не стал есть "{food.name.lower()}"')
        self.die()

    def die(self):
        self.alive = False


class Mammal(Animal):
    ...


class Predator(Animal):
    ...


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
