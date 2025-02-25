# по задаче - декоратор is_prime именно распечатывает "простое" или "составное"
# поэтому я это именно запринтил, а не вернул.
# можно было бы сделать ещё так: return f'{num_type}\n{num}'
# или так: return num, num_type. далее уже работать с этими значениями вне функции


def is_prime(func):
    def wrapper(*args, **kwargs) -> int:
        num, num_type = func(*args, **kwargs), 'Простое'
        if num > 1:  # отрицательные, ноль и единица - ничего не принтим
            for i in range(2, num):
                if num % i == 0:
                    num_type = 'Составное'
                    break
            print(num_type)
        return num
    return wrapper


@is_prime
def sum_three(a: int, b: int, c: int) -> int:
    return a+b+c


print(sum_three(2, 3, 6), end='\n\n')
print(sum_three(1, 1, 2), end='\n\n')
print(sum_three(5, -15, 4), end='\n\n')
print(sum_three(10, -12, 3))
