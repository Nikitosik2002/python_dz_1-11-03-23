def degree_func(first_digit_a, second_digit_b, degree):
    if second_digit_b == 1:
        return print(f"Число получившееся при возведении в степень = {degree}")

    degree = degree * first_digit_a
    second_digit_b -= 1
    return degree_func(first_digit_a, second_digit_b, degree)


first_digit_a = int(input("Введите число A: "))
second_digit_b = int(input("Введите число B: "))
degree_func(first_digit_a, second_digit_b, degree=first_digit_a)
