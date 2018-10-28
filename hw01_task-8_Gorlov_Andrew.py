__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 8. Определить, является ли год, который
        ввел пользователь, високосным или невисокосным. '''

year = int(input('Введите год: '))

if year % 400 == 0:
    print('Год {} является високосным'.format(year))
elif year % 100 != 0 and year % 4 == 0:
    print('Год {} является високосным'.format(year))
else:
    print('Год {} невисокосный!'.format(year))
