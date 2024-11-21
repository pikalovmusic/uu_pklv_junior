from math import inf


def divide(first, second):
    match second:
        case 0: return inf
        case default: return first / second
