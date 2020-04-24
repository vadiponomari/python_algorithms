"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
 При этом каждое число представляется как коллекция, элементы которой — цифры числа.
  Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
"""

from collections import deque

first = deque(input("Введите число 1: "))
second = deque(input('Введите число 2: '))
order = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

if len(first) > len(second):
  first, second = second, first
summa = deque()
second.reverse()
j = -1
k = 0
for i in second:
  one = order.index(i)
  two = order.index(first[j])
  summa.append(order[(one + two + k) % 16])
  if (one + two) > 15:
    k = 1
  else:
    k = 0
  j -= 1
  if j == -len(first)-1:
    break

diff = len(second) - len(first)

if diff:
    summa1 = deque()
    second.reverse()
    for i in range(diff):
        summa1.append(order[(order.index(second[i]) + k) % 16])
        if order.index(second[i]) + 1 > 15:
            k = 1
        else:
            k = 0
summa1.reverse()
for i in summa1:
    summa.append(i)


if k == 1:
    summa.append('1')
summa.reverse()
print(summa)




