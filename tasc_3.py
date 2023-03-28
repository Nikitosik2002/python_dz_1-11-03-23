def inverse_number_func(user_number, new_number):
    if len(str(user_number)) == 1:
        return print(*(new_number + [user_number]), sep='')
    last_digit = user_number % 10
    new_number.append(last_digit)
    user_number //= 10
    return inverse_number_func(user_number, new_number)


new_number = []
user_number = int(input("Введите число:"))
inverse_number_func(user_number, new_number)
