ticket_number = input("Введите номер билета: ")
ticket_number_left = \
    int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
ticket_number_right = \
    int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

if ticket_number_left == ticket_number_right:
    print("Ваш билет счастливый")
else:
    print("Ваш билет не является счастливым")

