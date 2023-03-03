"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet
lst1 = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(lst1, stdout=subprocess.PIPE)
print(YA_PING.stdout)
for line in YA_PING.stdout:
    res1 = chardet.detect(line)
    print(line.decode(res1['encoding']))
lst2 = ['ping', 'youtube.com']
YT_PING = subprocess.Popen(lst2, stdout=subprocess.PIPE)
print(YT_PING.stdout)
for line in YT_PING.stdout:
    res2 = chardet.detect(line)
    print(line.decode(res2['encoding']))
