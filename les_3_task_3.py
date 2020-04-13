"""
3) В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

size = 10
item_max = 100
item_min = 0

array = [random.randint(item_min, item_max) for _ in range(size)]

array_min = array[0]
array_max = array[0]
index_min = 0
index_max = 0
print(array)
for i in range(1, len(array)):
    if array[i] < array_min:
        array_min = array[i]
        index_min = i
    if array[i] > array_max:
        array_max = array[i]
        index_max = i
array[index_min], array[index_max] = array[index_max], array[index_min]
print(array)
