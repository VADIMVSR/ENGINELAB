import re

def is_correct_mobile_phone_ru(number):
    # Регулярное выражение для проверки номера телефона
    pattern = r'^(\+7|8)\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2,3}[\s-]?\d{2}$'

    # Проверяем номер телефона с помощью регулярного выражения
    return bool(re.match(pattern, number))

def main():
    # Чтение строки из стандартного ввода
    phone_number = input("Введите номер мобильного телефона: ")

    # Проверка корректности номера телефона
    if is_correct_mobile_phone_ru(phone_number):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
