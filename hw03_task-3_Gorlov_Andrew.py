__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 3. В массиве случайных целых чисел поменять местами минимальный и 
максимальный элементы.'''

import random

mas_num = [random.randint(1, 100) for n in range(9)]
print('Дан массив элементов: {}'.format(mas_num))

# Зададим первый элемент массива как значение минимума и максимума
m = 0
n = 0
min_num = mas_num[m]
max_num = mas_num[n]

# Определим минимальный и максимальный элемент
for i in mas_num[1:]:
    if min_num > i:
        min_num = i
        m = mas_num.index(i)
    if max_num < i:
        max_num = i
        n = mas_num.index(i)

# Поменяем местами минимальный и максимальный элементы
mas_num[m] = max_num
mas_num[n] = min_num
print('''Массив после того как у него поменяли местами максимальный и
минимальный элемент: {}'''.format(mas_num))
