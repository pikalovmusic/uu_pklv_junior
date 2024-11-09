calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str) -> tuple:
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string: str, list_to_search: list) -> bool:
    count_calls()
    string_to_search = ' '.join(list_to_search).lower()
    return string_to_search.__contains__(string.lower())


# Пример из урока (для проверки себя):
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
