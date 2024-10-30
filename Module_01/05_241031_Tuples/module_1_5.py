immutable_var = ('string1', 32, 5.5, True, 'string2', [3, 5, 7], 365, False, 0)
print(immutable_var)
print(immutable_var[3])
print(immutable_var[1:4])

# immutable_var[0] += '_changes'
# immutable_var[1] = 2
# immutable_var[2] = 2.1
# элементы данных типов являются неизменяемыми. Изменить в кортеже их мы не можем

immutable_var[5][1] = 25
print(immutable_var)  # список является изменяемым объектом и мы можем изменять его элементы даже внутри кортежа.
# а вот добавить в кортеж или удалить элементы мы уже не можем.

mutable_list = [2, 'string3', True, 7.1, 55, 'Evgeniy Pikalov']
mutable_list[0] = mutable_list[0] ** mutable_list[0]
mutable_list[1] += '_changed'
mutable_list[2] = False
mutable_list[3] += 6.24
mutable_list[4] *= 2
mutable_list[5] = '@%s' % mutable_list[5].replace(' ', '').lower()
print(mutable_list)  # как видно - элементы списка прекрасно изменяются
