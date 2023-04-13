"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
words = ['class', 'function', 'method']


def word_bytes(el):
    word = bytes(el, 'utf-8')
    return print(word), print(type(word)), print(len(word))


for el in words:
    word_bytes(el)
    print()
