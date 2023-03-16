n = int(input("Введите количество монет:"))
eagle = int(input("Введите количество орлов:"))
tails = n - eagle
if eagle > tails:
    print(f"Нужно перевернуть {tails} решек")
elif eagle == tails:
    print(f"Число орлов и решек равно, минимальное количество монет для "
    f"переворота = {eagle}")
else:
    print(f"Нужно перевернуть {eagle} орлов")