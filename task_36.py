def print_operation_table(operation, num_rows, num_сolumns):
    arr = [i*j for i in range(1, num_rows+1) for j in range(1, num_сolumns+1)]

    count = 0
    line_count = num_сolumns
    for el in arr:
        count += 1
        print(el, end=" ")
        if count == line_count:
            print("")
            line_count += num_сolumns


print_operation_table(lambda x, y: x*y,
                      num_rows=int(input("Введите число строк:")),
                      num_сolumns=int(input("Введите число столбцов:")))
