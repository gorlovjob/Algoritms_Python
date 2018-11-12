# __author__ = 'Горлов Андрей Гарриевич'

''' Задача № 2. Написать два алгоритма нахождения i-го по счёту простого числа.

    Без использования «Решета Эратосфена»;
    Используя алгоритм «Решето Эратосфена»

Примечание ко всему домашнему заданию: Проанализировать скорость и 
сложность алгоритмов. Результаты анализа сохранить в виде комментариев
 в файле с кодом. '''

import cProfile

'''
# Функция с использованием алгоритма "Решето Эратосфена"
def fun_with_er(n):
    if n > 1:
        sieve = [i for i in range(n * n)]

        sieve[1] = 0

        for i in range(2, n * n):
            if sieve[i] != 0:
                j = i + i
                while j < n * n:
                    sieve[j] = 0
                    j += i

        res = [i for i in sieve if i != 0]
        return res[n-1]
    elif n == 1:
        return 2
'''


# cProfile.run("fun_with_er(100)")
# 1    0.031    0.031    0.034    0.034 hw04_task-2_Gorlov_Andrew.py:17(fun_with_er)
# cProfile.run("fun_with_er(200)")
# 1    0.101    0.101    0.114    0.114 hw04_task-2_Gorlov_Andrew.py:17(fun_with_er)
# cProfile.run("fun_with_er(300)")
# 1    0.258    0.258    0.291    0.291 hw04_task-2_Gorlov_Andrew.py:17(fun_with_er)
# cProfile.run("fun_with_er(500)")
# 1    0.569    0.569    0.650    0.650 hw04_task-2_Gorlov_Andrew.py:17(fun_with_er)
# cProfile.run("fun_with_er(750)")
# 1    1.395    1.395    1.595    1.595 hw04_task-2_Gorlov_Andrew.py:17(fun_with_er)
# cProfile.run("fun_with_er(1000)")
# 1    2.521    2.521    2.793    2.793 hw04_task-2_Gorlov_Andrew.py:17(fun_with_er)
# cProfile.run("fun_with_er(2000)")
# 1   10.599   10.599   11.892   11.892 hw04_task-2_Gorlov_Andrew.py:17(fun_with_er)

# Алгоритм имеет квадратичную сложность.


# Функция БЕЗ алгоритма "Решето Эратосфена"
def fun_without_er(n):
    count_n = 0
    if n > 1:
        list_num = [i for i in range(2, n * n)]

        for i in list_num:
            count = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1

            if count == 2:
                sim = i
                count_n += 1

            if count_n == n:
                break

        return sim
    elif n == 1:
        return 2

# cProfile.run("fun_without_er(100)")
# 1    0.063    0.063    0.065    0.065 hw04_task-2_Gorlov_Andrew.py:55(fun_without_er)
# cProfile.run("fun_without_er(200)")
# 1    0.324    0.324    0.332    0.332 hw04_task-2_Gorlov_Andrew.py:55(fun_without_er)
# cProfile.run("fun_without_er(300)")
# 1    0.868    0.868    0.887    0.887 hw04_task-2_Gorlov_Andrew.py:55(fun_without_er)
# cProfile.run("fun_without_er(500)")
# 1    2.380    2.380    2.438    2.438 hw04_task-2_Gorlov_Andrew.py:55(fun_without_er)
# cProfile.run("fun_without_er(750)")
# 1    6.174    6.174    6.259    6.259 hw04_task-2_Gorlov_Andrew.py:55(fun_without_er)
# cProfile.run("fun_without_er(1000)")
# 1   12.043   12.043   12.265   12.265 hw04_task-2_Gorlov_Andrew.py:55(fun_without_er)
# cProfile.run("fun_without_er(2000)")
# 1   60.782   60.782   61.402   61.402 hw04_task-2_Gorlov_Andrew.py:55(fun_without_er)

# Алгоритм также имеет квадратичную сложность.

## Вывод: в результате анализа двух алгоритмов видно, что функция с использованием
# алгоритма "Решето Эратосфена" работает в разы быстрее, чем вторая функция.
