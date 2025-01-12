from time import sleep
from datetime import datetime
import threading


def wite_words(word_count: int, file_name: str):
    file = open(file_name, 'a', encoding='utf-8')

    for word in range(1, word_count+1):
        file.write(f'Какое-то слово № {word}\n')
        sleep(0.1)

    file.close()
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_elapsed = datetime.now()-time_start
print(f'Работа функций: {time_elapsed}')


thread1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))

time_start = datetime.now()
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
time_elapsed = datetime.now()-time_start
print(f'Работа потоков: {time_elapsed}')
