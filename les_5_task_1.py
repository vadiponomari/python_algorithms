"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
 для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import namedtuple

all_comps = []
total_profit = 0
Company = namedtuple('Company', ['name', 'Q1', 'Q2', 'Q3', 'Q4', 'annual'])
num = int(input("Ведите число предприятий:"))
for i in range(num):
    name = input(f'Название компании {i + 1} ')
    profit = []
    for j in range(4):
        q = int(input(f'Прибыль за квартал {j + 1}: '))
        profit.append(q)
    name = Company(name=name, Q1=profit[0], Q2=profit[1], Q3=profit[2], Q4=profit[3], annual=sum(profit))
    total_profit += name.annual
    all_comps.append(name)
total_profit /= num
below_avg = []
above_avg = []
for i in range(num):
    if all_comps[i].annual < total_profit:
        below_avg.append(all_comps[i].name)
    elif all_comps[i].annual > total_profit:
        above_avg.append(all_comps[i].name)
print(f'Средняя прибыль за год для всех предприятий= {total_profit}')
print(f'список компаний с прибылью ниже среднего: \n {below_avg}')
print(f'список компаний с прибылью ниже среднего: \n {above_avg}')
print(all_comps)
print(f'Средняя прибыль за год для всех предприятий= {total_profit}')
