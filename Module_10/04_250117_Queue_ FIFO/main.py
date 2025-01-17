from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Guest(Thread):
    def __init__(self, name: str):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Table:
    def __init__(self, number: int, guest: Guest = None):
        self.number = number
        self.guest = guest


class Cafe:
    def __init__(self, *tables: Table):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests: Guest):
        for guest in guests:

            if not self.__free_tables():
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                continue

            for table in self.tables:
                if table.guest is None:
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest
                    table.guest.start()
                    break

    def discuss_guests(self):
        while not self.__free_all_tables():
            for table in self.tables:
                if not table.guest is None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        table.guest = None
                        print(f'Стол номер {table.number} свободен')

                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(
                        f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

    def __free_tables(self) -> bool:
        for table in self.tables:
            if table.guest is None:
                return True
        return False

    def __free_all_tables(self):
        for table in self.tables:
            if not table.guest is None:
                return False
        return True


# ПРОВЕРКА:

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
