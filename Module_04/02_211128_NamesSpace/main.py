def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
# inner_function()

# закомментил вызов inner_function() чтобы не мозолила глаза ошибка

# inner_function() - эта функция не в глобальной области видимости,
# результат выполнения - ошибка "NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?"
# вызвать inner_function() мы можем только из локального пространства имён test_function()
