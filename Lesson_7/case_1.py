"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    __color = ["red", "yellow", "green"]

    def __init__(self, param):
        self.param = "TrafficLight"

    def running(self, val):
        for el in val:
            if el == "red":
                print(el)
                time.sleep(7)
            elif el == "yellow":
                print(el)
                time.sleep(2)
            elif el == "green":
                print(el)
                time.sleep(4)
                return


color = ["red", "yellow", "green"]
a = TrafficLight(color)
a.running(color)
