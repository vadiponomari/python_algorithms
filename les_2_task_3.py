"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
def rec(number):
   if number<10:
      return number
   else:
      return int(str(number%10) + str(rec(number//10)))
print(rec(3486))
