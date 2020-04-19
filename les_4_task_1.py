import random
import timeit
import cProfile


"""
из трех вариантов алгоритма наиболее предпочтителен второй, так как у него линейная сложность, 
в то время как у первого и третьего варианта квадратичная. 
"""

#  вариант 1
# def mode(size):
#     array = [random.randint(size * -10, size * 10) for _ in range(size)]
#     num = array[0]
#     frequency = 1
#     for i in range(len(array)):
#         spam = 1
#         for j in range(i + 1, len(array)):
#             if array[i] == array[j]:
#                 spam += 1
#             if spam > frequency:
#                 frequency = spam
#                 num = array[i]
#     return f'Число {num} встречается {frequency}' if frequency > 1 else "все элементы уникальны"


#print(timeit.timeit('mode(10)', number = 1000, globals = globals())) # 0.035494399999999995
# print(timeit.timeit('mode(100)', number = 1000, globals = globals())) # 0.7797797
# print(timeit.timeit('mode(1000)', number = 1000, globals = globals())) # 65.15466479999999
# print(timeit.timeit('mode(10000)', number = 1000, globals = globals())) #  долго грузилось, прервал
# Прослеживается квадратичня зависимость, увеличиваем n в 10 раз, а время выполнения алгоритма увеличивается 100 раз приблизительно.
# квадратичную завситсимость подтвердил cProfile




# cProfile.run('mode(1000)')

# 6631 function calls in 0.057 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.057    0.057 <string>:1(<module>)
#         1    0.055    0.055    0.057    0.057 les_4_task_1.py:7(mode)
#         1    0.000    0.000    0.002    0.002 les_4_task_1.py:8(<listcomp>)
#      1000    0.001    0.000    0.002    0.000 random.py:172(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:216(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:222(_randbelow)
#         1    0.000    0.000    0.057    0.057 {built-in method builtins.exec}
#      1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1625    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('mode(10000)')

# 63156 function calls in 6.707 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    6.707    6.707 <string>:1(<module>)
#         1    6.649    6.649    6.707    6.707 les_4_task_1.py:7(mode)
#         1    0.008    0.008    0.055    0.055 les_4_task_1.py:8(<listcomp>)
#     10000    0.017    0.000    0.039    0.000 random.py:172(randrange)
#     10000    0.008    0.000    0.047    0.000 random.py:216(randint)
#     10000    0.013    0.000    0.022    0.000 random.py:222(_randbelow)
#         1    0.000    0.000    6.707    6.707 {built-in method builtins.exec}
#     10001    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#     10000    0.004    0.000    0.004    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13150    0.005    0.000    0.005    0.000 {method 'getrandbits' of '_random.Random' objects}




# Вариант 2
# def mode2(size):
#     array = [random.randint(size * -10, size * 10) for _ in range(size)]
#     counter = {}
#     frequency = 1
#     num = None
#     for item in array:
#         if item in counter:
#             counter[item] += 1
#         else:
#             counter[item] = 1
#         if counter[item] > frequency:
#             frequency = counter[item]
#             num = item
#     if num is not None:
#         return f'Число {num} встречается {frequency}'
#     else:
#         return "Все элементы уникальны"

# print(timeit.timeit('mode2(10)', number = 1000, globals = globals())) # 0.0354333
# print(timeit.timeit('mode2(100)', number = 1000, globals = globals())) # 0.2674852
# print(timeit.timeit('mode2(1000)', number = 1000, globals = globals())) # 2.3216422000000003
# print(timeit.timeit('mode2(10000)', number = 1000, globals = globals())) #  22.0358209
# в этом варианте явно прослеживается линейная зависимость мы увеличиваем n в 10 раз и время растет в 10 раз,
# этот вариант даёт явный прирост в скорости, особенно с ростом числа n.


# cProfile.run('mode2(10000)')
#
# 53171 function calls in 0.036 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.036    0.036 <string>:1(<module>)
#         1    0.002    0.002    0.036    0.036 les_4_task_1.py:112(mode2)
#         1    0.005    0.005    0.033    0.033 les_4_task_1.py:113(<listcomp>)
#     10000    0.011    0.000    0.023    0.000 random.py:172(randrange)
#     10000    0.005    0.000    0.028    0.000 random.py:216(randint)
#     10000    0.008    0.000    0.012    0.000 random.py:222(_randbelow)
#         1    0.000    0.000    0.036    0.036 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13166    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}






# вариант 3
def mode_3(size):
    array = [random.randint(size * -10, size * 10) for _ in range(size)]

    our_values = set(array)
    frequencies = []
    for i in our_values:
        count = 0
        for j in range(len(array)):
            if array[j] == i:
                count += 1
        frequencies.append([i, count])

    num = frequencies[0][0]
    num_times = frequencies[0][1]
    for i in range(1, len(frequencies)):
        if frequencies[i][1] > num_times:
            num_times = frequencies[i][1]
            num = frequencies[i][0]
    if num_times > 1:
        return f'{num} наша мода'
    else:
        return f'Все элементы массива уникальны'



#print(timeit.timeit('mode_3(10)', number = 1000, globals = globals())) # 0.14778190000000002
#print(timeit.timeit('mode_3(100)', number = 1000, globals = globals())) # 1.1394114000000002
#print(timeit.timeit('mode_3(1000)', number = 1000, globals = globals())) # 85.683028
#print(timeit.timeit('mode_3(10000)', number = 1000, globals = globals())) # не дождался

# наименее оптимальный вариант и с точки зрения скорости и сточки зрения памяти, так как создаются дополнительные объекты множество и массив
# также наблюдается квадратичная сложность.
# cProfile.run('mode_3(1000)')


# 7549 function calls in 0.077 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.077    0.077 <string>:1(<module>)
#         1    0.074    0.074    0.077    0.077 les_4_task_1.py:124(mode_3)
#         1    0.000    0.000    0.002    0.002 les_4_task_1.py:125(<listcomp>)
#      1000    0.001    0.000    0.002    0.000 random.py:172(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:216(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:222(_randbelow)
#         1    0.000    0.000    0.077    0.077 {built-in method builtins.exec}
#       968    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       967    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1609    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



#cProfile.run('mode_3(100


# 72553 function calls in 9.122 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    9.122    9.122 <string>:1(<module>)
#         1    9.077    9.077    9.121    9.121 les_4_task_1.py:124(mode_3)
#         1    0.004    0.004    0.029    0.029 les_4_task_1.py:125(<listcomp>)
#     10000    0.010    0.000    0.020    0.000 random.py:172(randrange)
#     10000    0.004    0.000    0.024    0.000 random.py:216(randint)
#     10000    0.007    0.000    0.011    0.000 random.py:222(_randbelow)
#         1    0.000    0.000    9.122    9.122 {built-in method builtins.exec}
#      9738    0.012    0.000    0.012    0.000 {built-in method builtins.len}
#      9737    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13073    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}