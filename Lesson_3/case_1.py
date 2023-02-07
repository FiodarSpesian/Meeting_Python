"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

mon = int(input(f'Enter number of month: '))
if 0 < mon <= 12:
    seasons = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring",
               6: "summer", 7: "summer", 8: "summer",
               9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
    print(f"Season of your month is {seasons[mon]}")
else:
    print("Enter correct number of month")

