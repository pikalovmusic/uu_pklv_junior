first, second, third = input('Введите число 1: '), input('Введите число 2: '), input('Введите число 3: ')

if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
