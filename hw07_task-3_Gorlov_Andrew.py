__author__ = 'Горлов Андрей Гарриевич'

''' Задача № 3. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найти в массиве медиану. Медианой называется
элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше ее.

Задачу можно решить без сортировки исходного массива. Но если это 
слишком сложно, то используйте метод сортировки, который не 
рассматривался на уроках. '''

import random


def fi_med(array):
    ''' Функция определения медианы массива '''

    # Берем по очереди каждый элемент массива и сравниваем его с каждым
    # элементом, кроме того, что взяли.
    for i in range(len(array) - 1):

        # Задаем счетчики элементов.
        left = 0
        right = 0
        equal = 0

        for j in range(len(array)):

            # Не сравниваем элемент сам с собой.
            if i != j:

                # Если i-й элемент больше j-го, то подразумевается, что j-й
                # должен стоять левее i-го. Если меньше - правее. Если равен,
                # он может быть как правее, так и левее. В зависимости от
                # результата, увеличиваем соответствующий счетчик.
                if array[i] > array[j]:
                    left += 1
                elif array[i] < array[j]:
                    right += 1
                elif array[i] == array[j]:
                    equal += 1

        # Если количество левых и правых элементов равно, то считаем, что
        # равные равномерно распределены справа и слева. Элемент считается медианой.
        if left == right:
            return array[i]

        # Если количество левых и правых элементов не равно - возможно,
        # равные распределены неравномерно. Если тождество ниже истинно, то
        # элемент считается медианой массива.
        else:
            if abs(left - right) - equal == 0:
                return array[i]


# Вставил функцию сортировки пузырьковым методом для проверки результатов.
'''def puz_sort(array):
    n = 1

    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

        # Проверка на отсортированность: если текущий элемент больше, следующего,
        # то stop увеличивается на единицу. Если stop равно количеству проверок,
        # то массив считается отсортированным и функция возвращает массив.
        stop = 0
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                stop += 1
        if stop == len(array) - 1:
            return array

    return array'''

SIZE = 7
array = [random.randint(- SIZE, SIZE) for i in range(2 * SIZE - 1)]

print('Сгенерированный массив: \n{}'.format(array))
print('Медианой массива является число: {}'.format(fi_med(array)))

# print('Отсортированный массив:\n{}'.format(puz_sort(array)))
