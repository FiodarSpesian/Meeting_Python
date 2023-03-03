"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
lst = ["разработка", "администрирование", "protocol", "standard"]
n_lst1 = []
n_lst2 = []
for el in lst:
    n_lst1.append(el.encode("utf-8"))
for el in n_lst1:
    n_lst2.append(el.decode("utf-8"))
print(lst)
print(n_lst1)
print(n_lst2)