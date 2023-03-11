user_number = input("Введите любое целое число: ")
all_summ = 0
for el in user_number:
    count = int(el)
    all_summ = all_summ + count

print(f"Сумма цифр в числе = {all_summ}")
