"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ["разработка", "администрирование", "protocol", "standard"]

for el in words:
    word = el
    encod = el.encode('utf-8')
    decod = encod.decode('utf-8')
    print(word, encod, decod, sep=" ::: ")
