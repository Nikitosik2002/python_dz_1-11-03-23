month = int(input("Введите номер месяца:"))
list_1 = ["Зима", "Весна", "Лето", "Осень"]

if month >= 1 and month <= 2 or month == 12:
    print(f"Сейчас {list_1[0]}")
elif month >= 3 and month <= 5:
    print(f"Сейчас {list_1[1]}")
elif month >= 6 and month <= 8:
    print(f"Сейчас {list_1[2]}")
elif month >= 9 and month <= 11:
    print(f"Сейчас {list_1[3]}")