import string

def is_palindrome(data):
    # Удаляем пробелы и приводим к нижнему регистру
    data = ''.join(c.lower() for c in data if c.isalnum())
    return data == data[::-1]

def test_is_palindrome():
    test_cases = [
        ("radar", True),
        ("level", True),
        ("hello", False),
        ("racecar", True),
        ("noon", True),
        ("python", False),
        ("", True),  # Пустая строка
        ("A", True),  # Односимвольная строка
        ("madam", True),  # Палиндром с нечетным количеством символов
        ("abba", True),  # Палиндром с четным количеством символов
        ("12321", True),  # Палиндром, содержащий только цифры
        ("A man a plan a canal Panama", True),  # Палиндром с пробелами и заглавными буквами
        ("Was it a car or a cat I saw?", True),  # Палиндром с пробелами, знаками препинания и заглавными буквами
        ("not a palindrome", False),  # Непалиндром с пробелами и заглавными буквами
        ("1234567890", False),  # Строка без палиндрома
        ("A man, a plan, a canal, Panama", True),  # Палиндром с пробелами, запятыми и заглавными буквами
        ("Mr. Owl ate my metal worm", True),  # Палиндром с пробелами, точками и заглавными буквами
    ]

    for data, expected in test_cases:
        result = is_palindrome(data)
        if result == expected:
            print("YES")
        else:
            print("NO")
            return

test_is_palindrome()
