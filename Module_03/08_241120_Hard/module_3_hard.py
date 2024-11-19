def calculate_structure_sum(data):
    result = 0
    for item in data:
        if isinstance(item, int):
            result += item
        elif isinstance(item, str):
            result += len(item)
        else:
            if isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
                result += calculate_structure_sum(item)
            elif isinstance(item, dict):
                result += calculate_structure_sum(item.items())
    return result


# проверка:
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

# пробовал с *args - но в таком виде эта функция мне нравится больше.
# Написано "можно использовать", значит не обязательно.
# Рекурсивный вызов реализован
