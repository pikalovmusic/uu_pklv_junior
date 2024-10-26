homeworks_count = 12
hours_spent_count = 1.5
course_name = 'Python'
time_for_one_task = hours_spent_count / homeworks_count

print('Курс:', course_name + ',', 'всего задач:', str(homeworks_count) + ',', 'затрачено часов:',
               str(homeworks_count) + ',', 'среднее время выполнения:', time_for_one_task, 'часа.')

# Output: Курс: Python, всего задач: 12, затрачено часов: 12, среднее время выполнения: 0.125 часа.

# Можно сделать среднее время в минутах: time_for_one_task = (hours_spent_count*60)/homeworks_count
