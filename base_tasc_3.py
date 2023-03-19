def print_func(name, surname, year_of_birth, city, email, telephone_number):
    print(F"{name} {surname} {year_of_birth} года рождения, проживает в городе"
          F" {city} \nemail: {email}, телефон: {telephone_number}")


name = input("Введите свое имя:")
surname = input("Введите свою фамилию:")
year_of_birth = int(input("Введите год своего рождения:"))
city = input("Введите свой город:")
email = input("Введите свой E-mail адрес:")
telephone_number = input("Введите свой номер:")
print_func(name=name, surname=surname, year_of_birth=year_of_birth,
           city=city, email=email, telephone_number=telephone_number)
