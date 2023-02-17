"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random
mmin = int(input("введите значение минимума: "))
mmax = int(input("введите значение максимума: "))
my_lst = [random.randrange(1, 50) for i in range(20)]
print(my_lst)


def find_index(mn, mx, lst, i=0):
    if i == len(lst):
        return
    if mn < lst[i] < mx:
        print(i)
    i += 1
    find_index(mn, mx, lst, i)


find_index(mmin, mmax, my_lst)
