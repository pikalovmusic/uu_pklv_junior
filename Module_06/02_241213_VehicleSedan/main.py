class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'blue', 'black', 'white', 'silver']

    def __init__(self, owner_name: str, model: str, color: str, engine_power: int):
        self.owner = owner_name
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color.lower()

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power} hp'

    def get_color(self):
        return f'Цвет: {self.__color.capitalize()}'

    def print_info(self):
        print('%s\n%s\n%s\nВладелец: %s' % (self.get_model(),
              self.get_horsepower(), self.get_color(), self.owner.capitalize()))

    def set_color(self, new_color: str):
        if new_color.lower() not in self.__COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на "{new_color.lower().capitalize()}"')
            return
        self.__color = new_color.lower()


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# для проверки:
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()
