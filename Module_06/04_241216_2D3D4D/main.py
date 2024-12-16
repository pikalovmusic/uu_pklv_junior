from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int):
        self.__sides = sides
        self.__color = color
        self.filled = False

    def fill(self):
        self.filled = True

    def get_color(self) -> list:
        return list(self.__color)

    def get_sides(self) -> list:
        return list(self.__sides)

    def set_color(self, r=0, g=0, b=0):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def set_sides(self, *new_sides: int):
        if self.__is_valid_sides(new_sides):
            self.__sides = tuple(new_sides)

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
            return False
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            return False
        return True

    def __is_valid_sides(self, sides: tuple) -> bool:
        if len(sides) != self.sides_count:
            return False

        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False

        return True

    def __len__(self) -> int:
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = (1)

        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0]/pi*2

    def get_square(self) -> float:
        return pi*self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = (1, 1, 1)

        super().__init__(color, *sides)

    def get_square(self) -> float:
        sides = self.get_sides()
        a, b, c = sides[0], sides[1], sides[2]
        p = (a+b+c)/2
        return sqrt(p*(p-a)*(p-b)*(p-c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = (1)
        sides = sides*self.sides_count
        super().__init__(color, *sides)

    def get_volume(self) -> int:
        return self.get_sides()[0]**3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
