"""
Задание 2.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.
Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""
number = int(input(f'Enter positive integer: '))
max_my = number % 10
temp_my = 0
val = number % 10
if number > 0:
    while val != 0:
        temp_my = number % 10
        if max_my < temp_my:
            max_my = temp_my
        number = number // 10
        val = number % 10
    print(f'The biggest value of number: {max_my}')
else:
    print('error: entered number is wrong. Enter positive number. ')
