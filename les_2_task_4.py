"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

"""
def df(n):
    if n < 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        number = 1
        sum = 1
        for i in range(1,n):
            number = number /-2
            sum += number
        print (sum)


df(1)