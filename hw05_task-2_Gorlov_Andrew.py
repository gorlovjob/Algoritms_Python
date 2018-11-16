__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 2. Написать программу сложения и умножения двух
шестнадцатеричных чисел. При этом каждое число представляется
как массив, элементы которого это цифры числа. Например,
пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
[‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: для решения задач попробуйте применить какую-нибудь 
коллекцию из модуля collections '''

from collections import deque

p = 0
lst_sum = deque([])
lst_mult = deque([])
lst_tmp = deque([])
lst_tmp2 = []
lst_tmp3 = deque([])


def full_lst(lst_1, lst_2):
    ''' Функция добавляет нули вперед списка, чтобы длины двух
        списков были одинаковыми. Это нужно, чтобы было что складывать
        "в столбик" '''
    while len(lst_1) != len(lst_2):
        lst_2.appendleft('0')
    return lst_2


# Список возможных шестнадцатиричных значений
hex_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

lst_1 = deque([i for i in input('Введите первое число (буквы вводите заглавными): ')])
lst_2 = deque([i for i in input('Введите второе число (буквы вводите заглавными): ')])

# Выравниваем длины списков, заполняя их нулями слева.
if len(lst_1) > len(lst_2):
    lst_2 = full_lst(lst_1, lst_2)
elif len(lst_1) < len(lst_2):
    lst1 = full_lst(lst_2, lst_1)

# Превращаем шестнадцатиричные цифры в числовые индексы, складываем их.
# Сумма индексов - это индекс новой шестнадцатиричной цифры.
# p - это десяток, который остается "в уме" при сложении в
# столбик и прибавляется к следующей цифре.
# Полученные при сумме цифры складываются в число в списке lst_sum
for i in range(1, len(lst_1) + 1):
    ind_sum = hex_num.index(lst_1[-i]) + hex_num.index(lst_2[-i]) + p
    if ind_sum > 15:
        p = ind_sum // 16
        ind_sum = ind_sum % 16
    else:
        p = 0
    lst_sum.appendleft(hex_num[ind_sum])
if p > 0:
    lst_sum.appendleft(hex_num[p])
    p = 0
print('Сумма чисел равна: {}'.format(lst_sum))

# Умножение производится аналогично сумме, по правилам умножения в столбик.
for i in range(1, len(lst_1) + 1):
    for j in range(1, len(lst_2) + 1):
        ind = hex_num.index(lst_1[-j]) * hex_num.index(lst_2[-i]) + p
        if ind > 15:
            p = ind // 16
            ind = ind % 16
        else:
            p = 0
        lst_tmp.appendleft(hex_num[ind])
    if p > 0:
        lst_tmp.appendleft(hex_num[p])
        p = 0
    # Сдвиг слагаемых по правилам умножения в столбик (справа вставляем нули)
    if i != 1:
        for j in range(1, i):
            lst_tmp.append('0')
    lst_tmp2.append(lst_tmp.copy())
    lst_tmp.clear()

# Три слагаемых, которые получились в результате умножения столбиком
# Выравнить до одинаковой длины, забив нулями.
for i in lst_tmp2:
    i = full_lst(lst_tmp2[-1], i)

# Первое слагаемое сразу перекладываем в результативный список
lst_mult = lst_tmp2[0]

# Суммируем слагаемые аналогично сумме выше.
for lst in lst_tmp2[1:]:
    for i in range(1, len(lst_mult) + 1):
        ind_sum = hex_num.index(lst_mult[-i]) + hex_num.index(lst[-i]) + p
        if ind_sum > 15:
            p = ind_sum // 16
            ind_sum = ind_sum % 16
        else:
            p = 0
        lst_tmp3.appendleft(hex_num[ind_sum])
    if p > 0:
        lst_tmp3.appendleft(hex_num[p])
        p = 0
    lst_mult = lst_tmp3.copy()
    lst_tmp3.clear()
print('Произведение чисел равно: {}'.format(lst_mult))
