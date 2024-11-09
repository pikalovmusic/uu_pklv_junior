def get_password(num: int):
    result = ''
    for symbol_1 in range(1, num):
        for symbol_2 in range(symbol_1 + 1, num):
            if num % (symbol_1 + symbol_2) == 0 or symbol_1 + symbol_2 == num:
                result += '%s%s' % (str(symbol_1), str(symbol_2))

    return result


while True:
    user_input = input('Введите число из первого поля: ')
    if user_input.lower() == 'exit':
        exit(0)

    print(f'Пароль: {get_password(int(user_input))}\n')

# опытным путём выявлено, что не обязательно перебирать число для пар от 1 до 20,
# для экономии ресурсов достаточно перебрать числа до значения num невключительно
# во втором цикле для числа b - от числа a+1
