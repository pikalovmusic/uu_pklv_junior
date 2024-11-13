def single_root_words(root_word: str, *other_words: str) -> list:
    same_words = list()
    for word in other_words:
        if word.lower().__contains__(root_word.lower()) or root_word.lower().__contains__(word.lower()):
            same_words.append(word)
    return same_words


# проверка:
result1 = single_root_words(
    'rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
