first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x[0])-len(x[1])
                for x in zip(first, second) if len(x[0]) != len(x[1]))

second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))

print(list(first_result))
print(list(second_result))
