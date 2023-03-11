income = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))

if income > costs:
    print("Выручка больше издержек, фирма работает в прибыль")
    result = income - costs
    print(f"Прибыль фирмы: {result}")
    profitability = result / income
    print(f"Рентабельность выручки: {profitability}")
    quantity_staffers = int(input("Введите численность сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника "
          f"= {result / quantity_staffers}")
elif income == costs:
    print("Фирма рабоает безубыточно ")
else:
    print("Издержки больше выручки, фирма работает в убыток")