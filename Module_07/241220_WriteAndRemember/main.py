def custom_write(file_name: str, strings: list) -> dict:
    strings_positions = dict()

    file = open(file_name, 'a', encoding='utf-8')

    for string_number in range(1, len(strings)+1):
        byte_number = file.tell()

        file.write(f'{strings[string_number-1]} \n')

        strings_positions[
            (string_number, byte_number)] = strings[string_number-1]

    file.close()
    return strings_positions


# proverka:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
