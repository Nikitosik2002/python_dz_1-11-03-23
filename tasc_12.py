s = int(input("Введите сумму X и Y: "))
p = int(input("Введите произведение X и Y: "))
for i in range(s):
    for j in range(p):
        if s == i + j and p == i * j:
            print(i,j)
