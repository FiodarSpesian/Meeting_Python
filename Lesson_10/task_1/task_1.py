"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""
import json
import re
lst = ["разработка", "сокет", "декоратор"]


def code_points(arr):
    with open("converter.json", "w", encoding="utf-8") as f_n:
        for el in arr:
            f_n.write(json.dumps(el))
    n_arr = []
    with open("converter.json", "r", encoding="utf-8") as f_n:
        n_arr.append(f_n.read().split('"'))
    res = []
    for el in n_arr:
        #print(el)
        for i in range(len(el)):
            if i % 2 != 0:
                #print(f"{i} = {el[i]}")
                res.append(el[i])
    return res


values = code_points(lst)
for i in range(len(lst)):
    print(f"{lst[i]} -- буквкееый формат")
    print(f"{values[i]} -- набор кодовых точек")


