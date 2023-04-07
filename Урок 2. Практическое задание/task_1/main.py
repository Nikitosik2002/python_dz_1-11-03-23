import re
import csv


def get_data(file, number_f):
    number_file = [number_f]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [
        ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    with open(file) as line:
        all_lines = line.read()
        os_prod_list.append(
            re.compile(r'Изготовитель системы:\s*\S*').findall(all_lines)[
                0].split()[2])
        os_name_list.append(
            re.compile(r'Название ОС:\s*\S*\s*\S*\s*').findall(all_lines)[
                0].split()[3])
        os_name_list.append(
            re.compile(r'Название ОС:\s*\S*\s*\S*\s*\d*').findall(all_lines)[
                0].split()[4])
        os_code_list.append(
            re.compile(r'Код продукта:\s*\S*').findall(all_lines)[0].split()[
                2])
        os_type_list.append(
            re.compile(r'Тип системы:\s*\S*').findall(all_lines)[0].split()[2])

        os_name_list[0: 2] = [' '.join(os_name_list[0: 2])]
        main_data = [
            *number_file,
            *os_prod_list,
            *os_name_list,
            *os_code_list,
            *os_type_list
        ]
        return main_data


def write_to_csv(file, res):
    with open(file, 'w') as f_n:
        write = csv.writer(f_n, delimiter=",", lineterminator="\r")
        write.writerow(["Изготовитель системы", "Название ОC", "Код продукта",
                        "Тип системы"])
        for line in res:
            write.writerow(line)


f_1 = get_data('info_1.txt', 1)
f_2 = get_data('info_2.txt', 2)
f_3 = get_data('info_3.txt', 3)

result = (f_1, f_2, f_3)

write_to_csv('new.csv', result)
