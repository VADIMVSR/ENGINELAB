import re

def is_correct_mobile_phone_number_ru(number):
    # Регулярное выражение для проверки номера телефона
    pattern = r'^(\+7|8)\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'

    # Проверяем номер телефона с помощью регулярного выражения
    return bool(re.match(pattern, number))

def test_is_correct_mobile_phone_number_ru():
    test_cases = [
        ("+7(900)1234567", True),
        ("+7 900 123 45 67", True),
        ("8(900)1234567", True),
        ("8 900 123-45-67", True),
        ("89001234567", True),
        ("+79111234567", True),
        ("+7 911 123-45-67", True),
        ("abc", False),                 # Некорректный формат номера
        ("+8(900)1234567", False),     # Неправильный код страны
        ("+7(800)123-4567", True),     # Неправильное количество цифр в номере
    ]

    for number, expected in test_cases:
        result = is_correct_mobile_phone_number_ru(number)
        if result == expected:
            print("YES")
        else:
            print("NO")
            return

test_is_correct_mobile_phone_number_ru()
