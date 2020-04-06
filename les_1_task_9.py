"""
9) Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

"""
print("Введите три разных числа")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if x > z:
    if y > x:
        print(f"Наше среднее x = {x}")
    else:
        if y > z:
            print(f"Наше среднее y = {y}")
        else:
            print(f"Наше среднее z = {z}")
else:
    if x < y:
        if y > z:
            print(f"Наше среднее z = {z}")
        else:
            print(f"Наше среднее y = {y}")
    else:
        print(f"Наше среднее x = {x}")

