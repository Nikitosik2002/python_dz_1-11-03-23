volume = int(input("Введите количество журавликов: "))
if volume % 6 == 0:
    p_and_s = volume // 3
    kate = p_and_s * 2
    p_and_s = p_and_s // 2
    print(f"{p_and_s} {kate} {p_and_s}")
else:
    print("Дети не могли сделать такое количество журавликов")