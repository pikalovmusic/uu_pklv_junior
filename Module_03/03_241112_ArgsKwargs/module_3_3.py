values_list = [9.3, True, 'Urban']
values_list_2 = ['other string', False]
values_dict = {'a': 1, 'b': '2.0', 'c': 3.0}


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()
print_params('urban')
print_params(25, c=False)
print_params(True, 7, 'string')

# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)
print_params(c=[1, 2, 3])

# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
print_params(*values_list)
print_params(**values_dict)

# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)

# -всё работает
