team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 2153.31451
tasks_total = score_1+score_2
time_avg = 45.2


def check_winner() -> str:
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return f'Победа команды "{team1}"'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return f'Победа команды "{team2}"'
    return 'Ничья!'


# Использование %:
print('В команде %s участников: %d !' % (team1, team1_num))
print('Итого сегодня в командах участников: %d и %d !' % (
    team1_num, team2_num))

# Использование format():
print('Команда {} решила задач: {} !'.format(team2, score_2))
# тут в задании ошибка. Было написано team1_time. Я заменил на team2_time
print('{1} решили задачи за {0} с !'.format(team2_time, team2))

# Использование f-строк:
challenge_result = check_winner()
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач,',
      f'в среднем по {time_avg} секунды на задачу!')
print(time_avg)
