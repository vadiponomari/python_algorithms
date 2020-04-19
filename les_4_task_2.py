# вторая версия алгоритма намного быстрее и имеет линейную сложность, а  решето Эратосфена квадратичную сложность.
# Также вторая версия алгоритма вне зависимости от n просто быстрее выполняется.
import timeit
import cProfile

# через решето Эратосфена
def sieve(n):
    array = [i for i in range(n * 10)]
    array[1] = 0
    for i in range(2, len(array)):
        if array[i] != 0:
            j = i + i
            while j < len(array):
                array[j] = 0
                j += i
        res = [i for i in array if array[i] != 0]
    return res[n - 1]


#print(timeit.timeit('sieve(10)', number = 1000, globals = globals())) # 0.7380042
#print(timeit.timeit('sieve(20)', number = 1000, globals = globals())) # 2.9782210000000005
#print(timeit.timeit('sieve(40)', number = 1000, globals = globals())) # 11.9817049
#print(timeit.timeit('sieve(80)', number = 1000, globals = globals())) #  45.4250746
# в данном варинте прослеживается квадратичная зависимость n увеличивается в два раза, а скорость в 4 раза, что Cprofile подтвердил.

# cProfile.run('sieve(100)')
# 3128 function calls in 0.084 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.084    0.084 <string>:1(<module>)
#       998    0.078    0.000    0.078    0.000 les_4_task_2.py:14(<listcomp>)
#         1    0.004    0.004    0.084    0.084 les_4_task_2.py:5(sieve)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:6(<listcomp>)
#         1    0.000    0.000    0.084    0.084 {built-in method builtins.exec}
#      2125    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('sieve(1000)')
# 34302 function calls in 6.227 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    6.227    6.227 <string>:1(<module>)
#      9998    6.154    0.001    6.154    0.001 les_4_task_2.py:14(<listcomp>)
#         1    0.070    0.070    6.227    6.227 les_4_task_2.py:5(sieve)
#         1    0.001    0.001    0.001    0.001 les_4_task_2.py:6(<listcomp>)
#         1    0.000    0.000    6.227    6.227 {built-in method builtins.exec}
#     24299    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# без решето Эратосфена
def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number
#print(timeit.timeit('search_prime(10)', number = 1000, globals = globals())) # 0.016326
#print(timeit.timeit('search_prime(20)', number = 1000, globals = globals())) # 0.034380999999999995
#print(timeit.timeit('search_prime(40)', number = 1000, globals = globals())) # 0.07641790000000001
#print(timeit.timeit('search_prime(80)', number = 1000, globals = globals())) # 0.2714082

# в этом варианте  прослеживается зависимость немного сложнее линейной мы увеличиваем n в 2 раза и время растет чуть больше, чем в 2 раза,
# cProfile.run('search_prime(1000)')

# 1003 function calls in 0.037 seconds

   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.037    0.037 <string>:1(<module>)
   #      1    0.037    0.037    0.037    0.037 les_4_task_2.py:53(search_prime)
   #      1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
   #    999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('search_prime(10000)')

# 10003 function calls in 4.426 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.426    4.426 <string>:1(<module>)
#         1    4.424    4.424    4.426    4.426 les_4_task_2.py:53(search_prime)
#         1    0.000    0.000    4.426    4.426 {built-in method builtins.exec}
#      9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}