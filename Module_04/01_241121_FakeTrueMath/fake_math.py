def divide(first, second):
    match second:
        case 0: return 'Ошибка'
        case default: return first / second
