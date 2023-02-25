"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [["Изготовитель ОС:", "Название ОС:", "Код продукта:", "Тип системы:"],
                 [os_prod_list, os_name_list, os_code_list, os_type_list]]
    for i in range(3):
        with open(f"info_{i+1}.txt") as file_obj:
            data = file_obj.read()
            os_prod_el = re.compile(r'Изготовитель ОС:\s*\S*')
            os_prod_list.append(os_prod_el.findall(data)[0].split()[2])
            os_name_el = re.compile(r'Название ОС:\s*\S*\s*\S*\s*\S*')
            os_name_list.append(os_name_el.findall(data)[0].split()[3:])
            os_code_el = re.compile(r'Код продукта:\s*\S*')
            os_code_list.append(os_code_el.findall(data)[0].split()[2])
            os_type_el = re.compile(r'Тип системы:\s*\S*')
            os_type_list.append(os_type_el.findall(data)[0].split()[2])
    return main_data


def write_to_csv():
    lst = get_data()
    with open("data_report.csv", "a", encoding="utf-8") as d_r:
        for i in range(len(lst)):
            if i == 0:
                for j in range(len(lst[i])):
                    d_r.writelines(f"{lst[i][j]}\t")
        d_r.writelines("\n")
        for i in range(len(lst)):
            if i > 0:
                for j in range(len(lst[i])):
                    d_r.writelines(f"{lst[i][j][0]}\t")
                d_r.writelines("\n")
                for j in range(len(lst[i])):
                    d_r.writelines(f"{lst[i][j][1]}\t")
                d_r.writelines("\n")
                for j in range(len(lst[i])):
                    d_r.writelines(f"{lst[i][j][2]}\t")


get_data()
write_to_csv()
