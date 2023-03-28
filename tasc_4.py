def summ_n_func(el_number, divisible, count, el_summ):
    if count == el_number:
        return print(f"Количество элементов: {el_number}, их сумма: {el_summ}")

    el_summ += divisible
    divisible /= -2
    count += 1
    return summ_n_func(el_number, divisible, count, el_summ)


summ_n_func(el_number=int(input("Введите количество элементов n:")),
            divisible=1, count=0, el_summ=0)