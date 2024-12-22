class WordsFinder:
    def __init__(self, *file_name: str):
        self.file_names = file_name

    def get_all_words(self) -> dict:
        all_words = dict()

        for file_name in self.file_names:
            with open(file_name) as file:
                words = list()

                for line in file:
                    line = line.lower()

                    for char in (',', '.', '=', '!', '?', ';', ':', ' - '):
                        line = line.replace(char, '')
                    words += line.split()

                all_words[file_name] = words

        return all_words

    def find(self, word: str) -> dict:
        result = dict()
        for file_name, words in self.get_all_words().items():
            word_count = 0
            for search_word in words:
                word_count += 1
                if search_word == word.lower():
                    result[file_name] = word_count
                    break
        return result

    def count(self, word: str) -> dict:
        result = dict()
        for file_name, words in self.get_all_words().items():
            word_count = 0
            for search_word in words:
                if search_word == word.lower():
                    word_count += 1
                    result[file_name] = word_count
        return result


# Проверка:
finder = WordsFinder('test.txt', 'if.txt', 'monday.txt')

print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))  # 3 слово по счёту
print(finder.count('teXT'))  # 4 слова teXT в тексте всег

print(finder.find('Child'))
print(finder.count('Child'))

print(finder.find('IF'))
print(finder.count('IF'))

print(finder.find('For'))
print(finder.count('For'))

print(finder.find('of'))
print(finder.count('of'))
