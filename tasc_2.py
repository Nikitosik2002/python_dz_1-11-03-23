def even_not_even_func(user_number, even_count, not_even_count):
    last_digit = user_number % 10
    user_number //= 10
    if last_digit % 2 == 0:
        even_count += 1
    else:
        not_even_count += 1

    if len(str(user_number)) == 1:
        if user_number % 2 == 0:
            even_count += 1
        else:
            not_even_count += 1
        return print(f"Количество четных и нечетных цифр в числе равно: "
                     f"({even_count}, {not_even_count})")

    return even_not_even_func(user_number, even_count, not_even_count)


user_number = int(input("Введите число:"))
even_not_even_func(user_number, even_count=0, not_even_count=0)
