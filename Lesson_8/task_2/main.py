"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json
import re

item = input("Товар:")
quantity = input("Количество:")
price = input("Цена:")
buyer = input("Покупатель:")
date = input("Дата оформления заказа:")


def write_order_to_json(itm, quan, pr, bur, dt):
    with open("orders.json", "r") as f_n:
        obj = json.load(f_n)
        dict_to_json = {"item:": itm,
                        "quantity:": quan,
                        "price:": pr,
                        "buyer:": bur,
                        "date:": dt}
        obj['orders'].append(dict_to_json)
    with open("orders.json", "w") as f_n:
        json.dump(obj, f_n, sort_keys=True, indent=4)


write_order_to_json(item, quantity, price, buyer, date)
