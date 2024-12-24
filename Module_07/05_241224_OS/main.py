import os
import time


def walking_dir(directory: str = '.') -> str:
    result = str()

    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime(
                "%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)

            result += 'Файл: %s\nПуть: %s\nРазмер: %d байт\nИзменён: %s\nРодительская директория: %s\n\n' % (
                file, filepath, filesize, formatted_time, parent_dir)

    return result


if __name__ == '__main__':
    print(walking_dir())
