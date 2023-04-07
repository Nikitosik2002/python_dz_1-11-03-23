vowels = {1: "ауоыиэяюёе"}
line = input("Введите ритм: ")
line = line.split()
len_count = 0
vowels_count = 0
array = []

while len_count != len(line):
    for i in line[len_count]:
        for j in vowels.get(1):
            if i == j:
                vowels_count += 1
    array.append(vowels_count)
    vowels_count = 0
    len_count += 1

first_el = array[0]
param_count = 0

for el in array:
    if el == first_el:
        param_count += 1

if param_count == len(line):
    print("Парам пам-пам")
else:
    print("Пам парам")
