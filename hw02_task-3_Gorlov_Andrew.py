__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 3. Сформировать из введенного числа обратное по
порядку входящих в него цифр и вывести на экран. Например,
если введено число 3486, то надо вывести число 6843.'''

new_num = ''

num = input('Введите число: ')
count = len(num)

for i in range(count):
    new_num = new_num + str(int(num) % 10)
    num = int(num) // 10
print(new_num)
