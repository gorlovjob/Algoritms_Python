__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 4. Найти сумму n элементов следующего ряда
чисел: 1 -0.5 0.25 -0.125 ... Количество элементов (n) вводится с клавиатуры.'''

range_j = [1]
n = int(input('Введите количество элементов ряда: '))

for i in range(1, n):
    range_j.append(range_j[i - 1] / (-2))
print('Сумма {} элементов ряда равна {}'.format(n, sum(range_j)))
