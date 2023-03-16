"""
Задание 1.
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = float(input('How many kilometers you run today: '))
b = float(input('How many kilometers you want to run: '))
counter = 1
while a < b:
    print(f'{counter} day: {round(a, 2)}')
    a = a + a / 10
    counter += 1

print(f'{counter} day: {round(a, 2)}')
print(f'Answer: on {counter} day sportsmen reach the goal - more than {round(a, 2)} km')