"""
7. Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""
def f(n):
    left_part = 0
    for i in range(n+1):
        left_part += i
    right_part = int(n*(n+1)/2)
    if left_part == right_part:
        print(f"Доказано {left_part} = {right_part}" )
    else:
        print("не доказано")

f(100)