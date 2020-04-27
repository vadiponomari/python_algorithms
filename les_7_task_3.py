"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
 Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
 в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки,
 который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random
m = 5
size = 2 * m + 1
array = [random.randint(0, 100) for _ in range(size)]
random.shuffle(array)

def median(array):
    n = len(array)
    print(array)
    for i in range(1,n):
        value = array[i]
        pos = i
        while pos > 0 and value < array[pos - 1]:
            array[pos] = array[pos - 1]
            pos -= 1
        array[pos] = value
    print(array)
    median = array[n // 2]
    print(f"Медиана в отсортированном массиве = {median}")

median(array)
