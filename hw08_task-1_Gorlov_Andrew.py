__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 1. Определение количества различных подстрок с использованием
хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких 
латинских букв. Требуется найти количество различных подстрок в этой строке. '''


def h_serc(string):
    sub_list = []
    for i in range(1, len(string)):
        j = 0
        for j in range(len(string) - j):
            sub_str = hash(string[j:j + i])
            if sub_str not in sub_list:
                sub_list.append(sub_str)
    return len(sub_list)


print(h_serc('abcde'))
print(h_serc('papa'))
