print(list('tauuda'))
print(tuple('tauuda'))
print(''.join(['t', 'a', 'u', 'u', 'd', 'a']))
print(bool(0))
print(bool(3))
print(bool("25sfes"))
print(bool(str()))

k = ['a', 'b', 'c', 'd', 'e']
v = [1, 2, 3, 4, 5]
print(dict(zip(k, v)))

numbers_1 = [5, 13, 68, 57, 4, 1, 11, 45, 7, 8, 10, 12, 15, 89, 43, 44]
strings_1 = ['51', 'wet', 'dry', '51', 'zal',
             '23', '51', 'dry', 'oop', 'wet', 'list']


def find_max(numbers: list) -> int:
    result = 0
    for num in numbers:
        if num > result:
            result = num
    return result


def check_even(numbers: list) -> int:
    result = 0
    for num in numbers:
        if num % 2 == 0:
            result += 1
    return result


def get_unique(items: list) -> list:
    # return list(set(items))
    unique = list()
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


print('MAX:', find_max(numbers_1))  # 89
print('EVENs:', check_even(numbers_1))  # 6
print('UNI:', get_unique(strings_1))
