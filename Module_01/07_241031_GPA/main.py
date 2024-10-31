grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# преобразуем множество в список и сортируем
students_alphabet = sorted(list(students))

# создаём пустой словарь
dict_gpa = dict()

# проходимся по списку студентов по индексу и находим среднее арифметическое списков из списка grades по тому же индексу
for i in range(0, len(students_alphabet)):
    dict_gpa[students_alphabet[i]] = sum(grades[i]) / len(grades[i])

print(dict_gpa)
