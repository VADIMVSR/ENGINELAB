import re

def is_palindrome(data):
    """
    Функция проверяет, является ли строка палиндромом.
    """
    # Удаление пробелов и знаков препинания из строки
    clean_data = re.sub(r'[^A-Za-z0-9]', '', data)
    return clean_data.lower() == clean_data[::-1].lower()

def run_tests():
    """
    Тестирование функции is_palindrome().
    """
    tests = [
        ("radar", True),
        ("level", True),
        ("hello", False),
        ("", True),  # Пустая строка считается палиндромом
        ("noon", True),
        ("A man, a plan, a canal, Panama", True),
        ("12321", True),
        ("racecar", True),
        ("apple", False),
        ("wasitacaroracatisaw", True),
        ("madam", True)
    ]

    for data, expected_result in tests:
        result = is_palindrome(data)
        if result == expected_result:
            print(f"Test passed for '{data}'")
        else:
            print(f"Test failed for '{data}'")

    # Печать результата тестов
    if all(result == expected_result for data, expected_result in tests):
        print("NO")
    else:
        print("YES")
# Ввод строки с клавиатуры
user_input = input("Введите строку для проверки на палиндром: ")

# Проверка введенной строки на палиндром
if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")

# Запуск тестов
run_tests()
