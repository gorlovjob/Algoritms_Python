__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 2. Посчитать четные и нечетные цифры введенного
натурального числа. Например, если введено число 34560, то у
него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''

count_ev = 0
count_odd = 0

num = input('Введите натуральное число: ')

for i in num:
    if int(i) % 2 == 0:
        count_ev += 1
    else:
        count_odd += 1
print('Четных цифр: {}. Нечетных цифр: {}.'.format(count_ev, count_odd))
