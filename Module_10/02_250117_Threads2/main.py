import threading

from time import sleep


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name}, на нас напали!')

        while enemies > 0:
            days += 1
            enemies -= self.power

            print(
                f'{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.')

            sleep(1)
            # это логичнее ставить в начале цикла. Но поставил так, чтобы вывод получился как в задании

        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


# Проверка:
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
