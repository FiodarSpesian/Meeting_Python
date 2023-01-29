"""
Задание 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
seconds = int(input("Enter time in seconds format: "))
minutes = seconds / 60
hours = minutes / 60
print(f"Time in format h:m:s - {round(hours, 2)} : {round(minutes, 2)} : {seconds}")
