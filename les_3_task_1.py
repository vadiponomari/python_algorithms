'''
1) В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9

'''
array = [i for i in range(2, 100)]
for num in range(2, 10):
    count = 0
    for i in range(len(array)):
        if array[i] % num == 0:
            count += 1
    print(f'числу {num} кратны {count} чисел диапазона')
