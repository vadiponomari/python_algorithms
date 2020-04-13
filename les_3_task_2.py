"""
2) Во втором массиве сохранить индексы четных элементов первого массива. Например,
если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

"""
import random

size = 10
item_min = 0
item_max = 10

array = [random.randint(item_min,item_max) for _ in range(size)]

result = []
for i, j in enumerate(array):
    if j % 2 == 0:
        result.append(i)
print(array)
print(result)
