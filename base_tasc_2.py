def del_func(arg_1, arg_2):
    return arg_1 / arg_2

arg_1 = int(input("Введите первое число:"))
arg_2 = int(input("Введите второе число:"))
try:
    check = arg_1 / arg_2
except ZeroDivisionError:
    print("Вы что? Пытаетесь делить на 0!")
else:
    print(del_func(arg_1, arg_2))