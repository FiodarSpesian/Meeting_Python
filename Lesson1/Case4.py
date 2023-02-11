"""
Задание 4.
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""
rev = int(input('Enter value of revenue: '))
cos = int(input('Enter value of costs: '))
if rev == cos:
    print('Your firm working on point out of costs.')
else:
    if rev > cos:
        print(f'Your firm is good! It is PROFIT!')
        prf = rev - cos
        print(f'Profit of your firm - {prf}')
        print(f'Profitability of your firm = {round(prf / rev, 3)}')
        ppl = int(input('Enter count of people working in your firm: '))
        print(f'Profit firm on one employee = {round(prf/ppl, 2)}')
    else:
        print('Your firm works bad :(')
