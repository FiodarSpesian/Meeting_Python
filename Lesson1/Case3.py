"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""
st_n = input("Enter your positive number n: ")
n = int(st_n)
st_res = ""
i = 0
res = 0
while i < n:
    st_res = st_res + st_n
    res = res + int(st_res)
    i += 1
print(f'Sum of your numbers of n: {res}')