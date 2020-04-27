'''Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
 в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;

● написать 3 варианта кода (один у вас уже есть);

● проанализировать 3 варианта и выбрать оптимальный;

● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

● написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а
 проявили творчество, фантазию и создали универсальный код для замера памяти.
'''
# Windows 10 x64 and Python 3.6.3
# Первый вариант задействует 3880 байт памяти, самый оптимальный с точки зрения затрат памяти, но скорости.
# второй вариант задействует 14016 байт, но зато он самый быстрый по скорости.
# третий вариант задействует 23548 байт, занимает больше всего в памяти и самый медленный, не стоит использовать.
import random
import sys

size = 100
array = [random.randint(size * -10, size * 10) for _ in range(size)]


def check_memory(*kwargs):
    summa = 0
    for element in kwargs:
        consumed = sys.getsizeof(element)
        summa += consumed
        if hasattr(element, "__iter__"):
            if hasattr(element, 'items'):
                for key, val in element.items():
                    summa += sys.getsizeof(key) + sys.getsizeof(val)
            elif not isinstance(element, str):
                for item in element:
                    summa += sys.getsizeof(item)
    print(f'Наш программа задействует= {summa} , байт')

#  вариант 1
# size = 100
# array = [random.randint(size * -10, size * 10) for _ in range(size)]
# num = array[0]
# frequency = 1
# for i in range(len(array)):
#     spam = 1
#     for j in range(i + 1, len(array)):
#         if array[i] == array[j]:
#             spam += 1
#         if spam > frequency:
#             frequency = spam
#             num = array[i]
# print( f'Число {num} встречается {frequency}' if frequency > 1 else "все элементы уникальны")
#check_memory(array, num,spam,frequency,i,j,size )


# вариант 2
# size = 100
# array = [random.randint(size * -10, size * 10) for _ in range(size)]
# counter = {}
# frequency = 1
# num = None
# for item in array:
#     if item in counter:
#         counter[item] += 1
#     else:
#         counter[item] = 1
#     if counter[item] > frequency:
#         frequency = counter[item]
#         num = item
# if num is not None:
#     print( f'Число {num} встречается {frequency}')
# else:
#     print( "Все элементы уникальны")
#
# check_memory(array,size,counter, frequency,item, num)

#вариант 3
size = 100
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
    print( f'{num} наша мода')
else:
    print( f'Все элементы массива уникальны')

check_memory(array,our_values, frequencies,count,i,j,num,num_times)