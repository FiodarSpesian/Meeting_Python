"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    count = 0

    def __init__(self):
        Worker.count += 1
        self.name = "Name"
        self.surname = "Surname"
        self.position = "Position"
        self._income = {}


class Position(Worker):
    def get_full_name(self, name, surname):
        self.name = name
        self.surname = surname
        return

    def get_total_income(self, wage, bonus):
        self._income["wage"] = wage
        self._income["bonus"] = bonus
        return


a = Position()
a.get_full_name("Fiodor", "Spetsyian")
a.get_total_income(20000, 5000)
print(f"{Worker.count}) Employee {a.name} {a.surname} income: {a._income}")
b = Position()
b.get_full_name("Sergey", "Kudin")
b.get_total_income(19000, 6000)
print(f"{Worker.count}) Employee {b.name} {b.surname} income: {b._income}")
