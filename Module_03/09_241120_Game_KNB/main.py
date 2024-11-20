from random import randint


HAND_GESTURES = ['камень', 'ножницы', 'бумага']

WINNER_COMBINATIONS = {'камень-ножницы': 0,
                       'ножницы-бумага': 1,
                       'бумага-камень': 2
                       }

score = [0, 0]
round = 0


def select_human() -> str:
    while True:
        gesture = input('Камень ножницы бумага, раз два три: ')
        if gesture.lower() in HAND_GESTURES:
            return gesture.capitalize()
        else:
            print('Попробуйте показать другой жест.')


def select_bot() -> str:
    return HAND_GESTURES[randint(0, 2)].capitalize()


def get_winner(gesture_human: str, gesture_bot: str) -> str:
    combination1 = f'{gesture_human.lower()}-{gesture_bot.lower()}'
    combination2 = f'{gesture_bot.lower()}-{gesture_human.lower()}'
    winner = str()

    if WINNER_COMBINATIONS.__contains__(combination1):
        winner = HAND_GESTURES[WINNER_COMBINATIONS.get(combination1)]
    elif WINNER_COMBINATIONS.__contains__(combination2):
        winner = HAND_GESTURES[WINNER_COMBINATIONS.get(combination2)]

    if winner == gesture_human.lower():
        score[0] += 1
        return 'Вы выиграли'
    elif winner == gesture_bot.lower():
        score[1] += 1
        return 'Выиграл компуктер'
    else:
        return 'Ничья'


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
        user_answer = input('Продолжить? да/нет: ')

        if user_answer.lower() == 'нет':
            exit(0)


# тут точка входа
print("\033c\033[3J", end="")
print('КАМЕНЬ НОЖНИЦЫ БУМАГА')
input("Для начала игры - нажмите enter_")
play()
