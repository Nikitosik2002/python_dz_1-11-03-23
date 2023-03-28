def summ_func(first_digit_a, second_digit_b, count):
    if second_digit_b == 0:
        return print(count)

    if first_digit_a != 0:
        first_digit_a -= 1
        count += 1
        return summ_func(first_digit_a, second_digit_b, count)
    elif second_digit_b != 0:
        second_digit_b -= 1
        count += 1
        return summ_func(first_digit_a, second_digit_b, count)

    return summ_func(first_digit_a, second_digit_b, count)


summ_func(first_digit_a=int(input("Введите число A: ")),
          second_digit_b=int(input("Введите число B: ")),
          count=0)
