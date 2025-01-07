class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start: int, stop: int, step: int = 1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')

        self.start, self.stop, self.step, self.i = start, stop, step, 0
        self.pointer = self.start

        # условие ниже добавлено, чтобы корректно работало как в случае с iter5:
        # в условиях задания вообще нет вывода у этого итератора
        # но чисто логически итерация должна идти от 10 до 1 (в случае iter5)
        if self.start > self.stop and self.step > 0:
            self.step = -self.step

    def __iter__(self):
        self.pointer, self.i = self.start, 0
        return self

    def __next__(self) -> int:
        self.i += 1
        if self.i == 1:
            return self.pointer

        self.pointer += self.step

        if (self.pointer > self.stop and self.step > 0) or (self.pointer < self.stop and self.step < 0):
            raise StopIteration()

        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')


# проверка:
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')

print()

for i in iter3:
    print(i, end=' ')

print()

for i in iter4:
    print(i, end=' ')

print()

for i in iter5:
    print(i, end=' ')

print()
