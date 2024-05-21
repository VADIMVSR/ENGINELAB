def check_phone_number(phone):
    try:
        phone = ''.join(filter(str.isdigit, phone))  # Убираем все символы-НЕцифры
        if len(phone) == 11 and phone.startswith('7'):  # Проверяем длину и начало номера
            return '+' + phone, "Формат верный"
        elif len(phone) == 10 and phone.startswith('8'):  # Проверяем длину и начало номера
            return '+7' + phone[1:], "Формат верный"
        else:
            raise ValueError("Неверное количество цифр")
    except ValueError:
        return 'error', "Неверный формат"

phone_number = input("Введите номер телефона: ")
formatted_phone_number, message = check_phone_number(phone_number)
print(formatted_phone_number, "-", message)
