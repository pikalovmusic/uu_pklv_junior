def personal_sum(numbers: list) -> tuple:
    result = int()
    incorrect_data = int()

    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {num}')
    return (result, incorrect_data)


def calculate_average(numbers: list) -> float:
    try:
        sum, incorrect = personal_sum(numbers)
        return sum/(len(numbers)-incorrect)
    except TypeError:
        print('В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0


# проверка:

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
