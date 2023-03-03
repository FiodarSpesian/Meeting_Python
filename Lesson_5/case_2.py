"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
number = list(input("Enter number: "))
print(number)


def even_odd(val, ev=0, od=0):
    if len(val) == 0:
        return print(f"Count of even: {ev} and odd: {od} values in number.")
    a = int(val.pop())
    print(a)
    if a % 2 == 1:
        od += 1
    elif a % 2 == 0:
        ev += 1
    even_odd(val, ev, od)


even_odd(number)
