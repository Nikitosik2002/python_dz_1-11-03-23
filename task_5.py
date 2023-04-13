"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet


def ping(website):
    args = ["ping", website]
    ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for el in ya_ping.stdout:
        default_coding = chardet.detect(el)
        print(el.decode(encoding=default_coding['encoding']))
    print(default_coding)


ping("yandex.ru")
ping("youtube.com")
