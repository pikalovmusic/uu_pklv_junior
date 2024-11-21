# файл game_functions.py так же нужно скачать/создать в той-же директории, что и main
#
# чтобы всё корректно отображалось - запускать через терминал (не через консоль PyCharm)
#
# 1. В PyCharm правой клавишей по директории с файлом -> Open In -> Terminal
# 2. Пишем: python имя_вашего_файла.py и жмём enter
#
# или через системный терминал: чтобы перейти в директорию пишем cd путь_к_директории enter
# затем пункт 2

from game_functions import *


def show_score():
    print("\033c\033[3J", end="")
    print(f'Раунд {round}\n')
    print(f'Человек   {score[0]}:{score[1]}   Компуктер\n')


def play():
    global round
    while True:
        round += 1
        show_score()

        gesture_human = select_human()
        gesture_bot = select_bot()
        winner = get_winner(gesture_human, gesture_bot)

        show_score()

        print('Вы:        %s\nКомпуктер: %s\n\n%s\n' %
              (gesture_human.lower(), gesture_bot.lower(), winner))

        # тут любое значение для продолжения подойдёт, кроме "нет"
        user_answer = input('Продолжить? enter/нет: ')

        if user_answer.lower() == 'нет':
            show_score()
            exit(0)


# тут точка входа
print("\033c\033[3J", end="")
print('КАМЕНЬ НОЖНИЦЫ БУМАГА')
input("Для начала игры - нажмите enter_")
play()
