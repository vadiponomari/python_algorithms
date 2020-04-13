"""
5) В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
 Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
 Это два абсолютно разных значения.
"""
import random

size = 10
item_max = 20
item_min = -20

array = [random.randint(item_min, item_max) for _ in range(size)]
max_among_min = 0
index_num = 0
print(array)
for i in range(len(array)):
    if array[i] < 0 and (max_among_min == 0 or array[i] > max_among_min):
        max_among_min = array[i]
        index_num = i

print(
    "нет отрицательных чисел в массиве" if max_among_min == 0 else f" максимальный отрицательный {max_among_min} в позиции {index_num}")
