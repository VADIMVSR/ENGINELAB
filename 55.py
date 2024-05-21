 
def check_phone_number(phone):
    try:
        phone = ''.join(filter(str.isdigit, phone))  # Убираем все символы-НЕцифры
        if phone.startswith('7'):
            if len(phone) == 11:  # Проверяем длину и начало номера
                operator_code = phone[1:4]
                if operator_code in ['910', '911', '912', '913', '914', '915', '916', '917', '918', '919',
                                     '980', '981', '982', '983', '984', '985', '986', '987', '988', '989']:
                    return '+7' + phone[1:], "МТС"
                elif operator_code in ['920', '921', '922', '923', '924', '925', '926', '927', '928', '929',
                                       '930', '931', '932', '933', '934', '935', '936', '937', '938', '939']:
                    return '+7' + phone[1:], "МегаФон"
                elif operator_code in ['902', '903', '904', '905',
                                       '960', '961', '962','963','964','965','966','967','968','969']:
                    return '+7' + phone[1:], "Билайн"
                else:
                    return '+7' + phone[1:], "не определяется оператор сотовой связи"
            else:
                raise ValueError("Неверное количество цифр")
        elif phone.startswith(('8', '+359', '+55', '+1')):
            if len(phone) == 10 or len(phone) == 12:  # Проверяем длину и начало номера
                return phone, "не определяется оператор сотовой связи"
            else:
                raise ValueError("Неверное количество цифр")
        else:
            raise ValueError("Не определяется код страны")
    except ValueError as e:
        return phone, str(e)

phone_number = input("Введите номер телефона: ")
formatted_phone_number, message = check_phone_number(phone_number)
print(formatted_phone_number, "-", message)
