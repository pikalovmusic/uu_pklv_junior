from random import randint
from time import sleep
import threading


class Bank:
    def __init__(self, balance=int()):
        self.lock = threading.Lock()
        self.balance = balance

    def deposit(self):
        for _ in range(100):
            value = randint(50, 500)
            self.balance += value
            print(f'Пополнение: {value}. Баланс: {self.balance}')
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for _ in range(100):
            value = randint(50, 500)
            print(f'Запрос на {value}')

            if value <= self.balance:
                self.balance -= value
                print(f'Снятие: {value}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

            sleep(0.001)  # тут тоже имитируем работу


# проверка:
bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
