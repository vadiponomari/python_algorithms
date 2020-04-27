"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
 Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортиро
"""
import random

size = 10
array = [random.randint(-100, 100) for _ in range(size)]
random.shuffle(array)
print(array)

def bubble_sort(array):
    for num in range(len(array)-1,0,-1):
         for i in range(num):
             if array[i]<array[i+1]:
                spam = array[i]
                array[i] = array[i+1]
                array[i+1] = spam
    print(array)
bubble_sort(array)
