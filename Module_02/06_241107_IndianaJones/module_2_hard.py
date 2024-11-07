def get_password(num: int):
    result = ''
    for a in range(1, num):
        for b in range(a + 1, num):
            if num % (a + b) == 0 or a + b == num: result += '%s%s' % (str(a), str(b))

    return result


while True:
    user_input = input('Введите число из первого поля: ')
    if user_input.lower() == 'exit': exit(0)

    print(f'Пароль: {get_password(int(user_input))}\n')

# опытным путём выявлено, что не обязательно перебирать число для пар от 1 до 20,
# для экономии ресурсов достаточно перебрать числа до значения num невключительно
# во втором цикле для числа b - от числа a+1
