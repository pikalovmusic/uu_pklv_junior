my_dict = {'Larisa': 32, 'Marina': 23, 'Natasha': 40, 'Angelina': 18, 'Violeta': 67}  # {Name:Age,}
print(my_dict)
print(my_dict.get('Marina', 'not found.'))
print(my_dict.get('Polina', 'not found.'))
my_dict.update({'Zinka': 45, 'Galina': 50})
print(my_dict.pop('Angelina'))
print(my_dict)

my_set = {3, 6, 3.14, 'urban', 3.14, 3, 6, 3.14, 1, 'urban', 6, 1, 3, 'urban', 1, }
print(my_set)
my_set.add(7)
my_set.add('G')
my_set.remove(3.14)
print(my_set)
