__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 4. Определить, какое число в массиве встречается чаще всего.'''

import random

mas_num = [random.randint(1, 9) for n in range(20)]
print('Дан массив элементов: {}'.format(mas_num))

# Одна переменная для числа, вторая - для количества его повторений
num = 0
count_num = 0

for i in set(mas_num):
    count = 0

    for j in mas_num:
        if i == j:
            count += 1

    if count > count_num:
        count_num = count
        num = i

print('''В массиве чаще всего встречается число {}.
Количество повторений: {}'''.format(num, count_num))
