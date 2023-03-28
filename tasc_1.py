def match_func():
    user_sign = input("Введите операцию (+, -, *, / или 0 для выхода):")
    if user_sign == "0":
        return

    if user_sign not in ["+", "-", "*", "/", 0]:
        return match_func()

    first_digit = int(input("Введите первую цифру:"))
    second_digit = int(input("Введите вторую цифру:"))
    if user_sign == "/" and second_digit == 0:
        try:
            ex = first_digit / second_digit
        except ZeroDivisionError:
            return print(f"невозможно делить на ноль")
        finally:
            match_func()

    match user_sign:
        case "+":
            print(first_digit + second_digit)
        case "-":
            print(first_digit - second_digit)
        case "*":
            print(first_digit * second_digit)
        case "/":
            print(first_digit / second_digit)
        case _:
            return match_func()
    return match_func()


match_func()