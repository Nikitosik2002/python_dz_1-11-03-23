N = int(input("Введите длинну массива:"))
X = int(input("Введите искомое число:"))
list_1 = []
count = 0
for el in range(N):
    list_1.append(el+1)
    if el + 1 == X:
        count += 1
print(list_1)
print(f"Число {X} повтаряется {count} раз")
