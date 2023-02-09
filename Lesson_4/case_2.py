"""
Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.
"""
num = int(input(f"Enter number: "))
lst = []
for i in range(num):
    if num % (i + 1) == 0:
        lst.append(i+1)
    for el in lst:
        if el % 2 == 0:
            lst.remove(el)
print(lst)
