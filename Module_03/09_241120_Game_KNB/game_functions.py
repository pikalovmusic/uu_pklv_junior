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
        gesture = input('Камень, ножницы, бумага?: ')
        if gesture.lower() in HAND_GESTURES:
            return gesture.capitalize()
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
