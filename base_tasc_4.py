def my_func(arg_1, arg_2, arg_3):
    list_1 = [arg_1, arg_2, arg_3]
    size = len(list_1)
    for i in range((size-1)):
        max = i
        for j in range(i+1, size):
            if list_1[max] < list_1[j]:
                max = j
        list_1[i], list_1[max] = list_1[max], list_1[i]
    return list_1[0] + list_1[1]


arg_1 = int(input("Введите первое число:"))
arg_2 = int(input("Введите второе число:"))
arg_3 = int(input("Введите третье число:"))

print(my_func(arg_1, arg_2, arg_3))