"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""
num = int(input("Enter count of values: "))


def sum_values(cnt, res=1, count=1, sum_my=1):
    if cnt <= count:
        return print(f"Count of values: {cnt}, summ: {sum_my} ")
    res /= (-2)
    sum_my += res
    count += 1
    sum_values(cnt, res, count, sum_my)


sum_values(num)
