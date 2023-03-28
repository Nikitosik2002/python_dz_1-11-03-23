from random import randint


def guess_number(random_number, attempts_number):
    if attempts_number == 10:
        return print(f'Вы не угадали загаданное число за 10 попыток, '
                     f'загаданное число:{random_number}')

    try:
        user_number = int(input("Введите угадоваемое число в "
                                "диапазоне от 0 до 100: "))
    except ValueError:
        print("Вы ввели не число, попробуйте снова...")
        return guess_number(random_number, attempts_number)

    if user_number > random_number:
        print(f"загаданное число меньше {user_number}")
    elif user_number < random_number:
        print(f"загаданное число больше {user_number}")
    else:
        print("Вы угадали загаданное число")
        return

    attempts_number += 1

    return guess_number(random_number, attempts_number)


random_number = randint(0, 100)
guess_number(random_number, attempts_number=0)
