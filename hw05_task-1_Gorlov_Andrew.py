__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 1. Пользователь вводит данные о количестве предприятий, их
наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого
предприятия.. Программа должна определить среднюю прибыль (за год для
всех предприятий) и вывести наименования предприятий, чья прибыль выше
среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего. '''

from collections import namedtuple

i = 0
company = namedtuple('company', 'name profit_1 profit_2 profit_3 profit_4')
list_company = []
all_pr = 0
lst_mo_av = ''
lst_le_av = ''

num = int(input('Введите количество предприятий: '))

while i != num:
    name = input('Введите название компании № {} --> '.format(i + 1))
    prof_1 = int(input('Прибыль за первый квартал --> '))
    prof_2 = int(input('Прибыль за второй квартал --> '))
    prof_3 = int(input('Прибыль за третий квартал --> '))
    prof_4 = int(input('Прибыль за четвертый квартал --> '))

    # Список кортежей с данными компаний
    list_company.append(company(name, prof_1, prof_2, prof_3, prof_4))

    # Общая прибыль всех компаний
    all_pr = all_pr + prof_1 + prof_2 + prof_3 + prof_4
    i += 1

# Средняя прибыль по всем предприятиям за год
all_av = all_pr / num / 4

for i in list_company:
    # Средняя прибыль одного предприятия
    av = (i.profit_1 + i.profit_2 + i.profit_3 + i.profit_4) / 4

    if av > all_av:
        lst_mo_av += i.name
    elif av < all_av:
        lst_le_av += i.name

print('Предприятия с прибылью выше среднего:', ', '.join(lst_mo_av))
print('Предприятия с прибылью ниже среднего:', ', '.join(lst_le_av))
