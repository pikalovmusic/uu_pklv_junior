def get_multiplied_digits(number: int) -> int:
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) <= 1:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))


# для проверки:
print(get_multiplied_digits(40203))  # 24
print(get_multiplied_digits(1))  # 1
print(get_multiplied_digits(23))  # 6
print(get_multiplied_digits(55223))  # 300
