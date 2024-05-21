import re
import string

def strip_punctuation_ru(data):
    # Получаем таблицу перевода, где все знаки пунктуации будут заменены на пробел
    translator = str.maketrans('', '', string.punctuation)
    # Применяем таблицу перевода к строке
    cleaned_data = data.translate(translator)
    # Разделяем строку на слова, используя регулярное выражение, которое учитывает последовательности пробелов
    cleaned_data = re.sub(r'\s+', ' ', cleaned_data)
    return cleaned_data.strip()

def test_strip_punctuation_ru():
    test_cases = [
        ("Привет, как дела?", "Привет как дела"),
        ("Это... тест?", "Это тест"),
        ("Привет! Как ты?", "Привет Как ты"),
        ("Он сказал: Привет!", "Он сказал Привет"),
        ("Почему? Потому, что!", "Почему Потому что"),
    ]

    for data, expected in test_cases:
        result = strip_punctuation_ru(data)
        if result == expected:
            print("YES")
        else:
            print("NO")

test_strip_punctuation_ru()
