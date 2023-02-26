"""
Создать не менее двух дескрипторов для атрибутов классов,
которые вы создали ранее в ДЗ
"""


class NotString:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_atr]

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError("Нельзя ввести значение кроме строки.")
        instance.__dict__[self.my_atr] = value

    def __delete__(self, instance):
        return instance.__dict__[self.my_atr]

    def __set_name__(self, owner, my_atr):
        self.my_atr = my_atr


class Worker:
    count = 0
    name = NotString()
    surname = NotString()

    def __init__(self):
        Worker.count += 1
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
a.get_full_name("Fiodar", "Spetsyian")
a.get_total_income(20000, 5000)
print(f"{Worker.count}) Employee {a.name} {a.surname} income: {a._income}")
b = Position()
b.get_full_name("Sergey", "Kudin")
b.get_total_income(19000, 6000)
print(f"{Worker.count}) Employee {b.name} {b.surname} income: {b._income}")