"""
4) Определить, какое число в массиве встречается чаще всего.
"""

import random

size = 20
item_max = 10
item_min = 0

array = [random.randint(item_min, item_max) for _ in range(size)]

our_values = set(array)
frequencies = []
for i in our_values:
    count = 0
    for j in range(len(array)):
        if array[j] == i:
            count += 1
    frequencies.append([i, count])

mode = frequencies[0][0]
num_times = frequencies[0][1]
for i in range(1, len(frequencies)):
    if frequencies[i][1] > num_times:
        num_times = frequencies[i][1]
        mode = frequencies[i][0]

# в случае нескольких мод
list_of_modes = []
list_of_modes.append(mode)
for i in range(len(frequencies)):
    if frequencies[i][1] == num_times and frequencies[i][0] != mode:
        list_of_modes.append(frequencies[i][0])

print(array)
print(our_values)
print(frequencies)
print(mode)
print(list_of_modes)
