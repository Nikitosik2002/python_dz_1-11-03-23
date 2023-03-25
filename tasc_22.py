from timeit import timeit

list_1 = []
list_2 = []
list_3 = []


def print_list(list_pr):
    size = int(input("Введите длинну массива:"))
    for el in range(size):
        list_pr.append(int(input(f"Введите {el} эллемент")))
    return list_pr


print_list(list_1)
print_list(list_2)

for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(i)


print(*list_3)

