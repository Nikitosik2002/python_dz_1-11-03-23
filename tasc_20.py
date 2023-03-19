dict_ru = {1: "АВЕИНОРСТ",
           2: "ДКЛМПУ",
           3: "БГЁЬЯ",
           4: "ЙЫ",
           5: "ЖЗХЦЧ",
           8: "ШЭЮ",
           10: "ФЩЪ"}

dict_en = {1: "AEIOULNSTR",
           2: "DG",
           3: "BCMP",
           4: "FHVWY",
           5: "K",
           8: "JX",
           10: "QZ"}

user_word = input("Введите слово:").upper()
# Словарь для проверки языка
language = ""
for i in range(ord('A'), ord('Z') + 1):
    language += chr(i)
# Если первая буква будет английской тогда будем вызывать английский словарь
language_count = 0
for i in language:
    if user_word[0] == i:
        language_count += 1
        break


def print_func(dict_1):
    total_count = 0
    for i in user_word:
        count = 1
        while count != 11:
            if count == 6:
                count = count + 2
            elif count == 9:
                count = count + 1
            for j in dict_1.get(count):
                if j == i:
                    total_count += count
            count += 1
    return total_count


if language_count == 1:
    print(print_func(dict_en))
else:
    print(print_func(dict_ru))
