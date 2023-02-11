"""
Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""
from random import randint
lst = [randint(0, 5) for n in range(10)]
print(f"Old list of values: {lst}")
lst = set(lst)
lst = list(lst)
print(f"New list of non repetitive values: {lst}")
