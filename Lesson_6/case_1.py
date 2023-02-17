"""
Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
a = int(input("первый элемент: "))
d = int(input("разность: "))
n = int(input("количество элементов: "))
array = list()


def math_progression(f_el, diff, count, lst):
    if count == 0:
        return lst.reverse()
    res = f_el + (count - 1) * diff
    lst.append(res)
    print(f"{count} element is {res}")
    count -= 1
    math_progression(f_el, diff, count, lst)


math_progression(a, d, n, array)
print(array)
