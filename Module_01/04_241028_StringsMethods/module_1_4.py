my_string = input('Введите текст: ')
print(len(my_string))

print(my_string.upper())  # верхний регистр
print(my_string.lower())  # нижний регистр

my_string = my_string.replace(' ', '')  # удаление пробелов (замена на пустую строку)
# задача была именно изменить строку, а не вывести её в изменённом виде, поэтому я не использовал print() на этом шаге

print(my_string[0])  # первый символ
print(my_string[-1])  # последний символ

# ВВОД: Urban University

# ВЫВОД:
# 16
# URBAN UNIVERSITY
# urban university
# UrbanUniversity
# U
# y
