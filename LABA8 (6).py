import re
import string

def strip_punctuation_ru(data):
    # Получаем таблицу перевода, где все знаки пунктуации будут заменены на пробелы
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    # Применяем таблицу перевода к строке
    cleaned_data = data.translate(translator)
    # Разделяем строку на слова, используя регулярное выражение, которое учитывает последовательности пробелов
    cleaned_data = re.sub(r'\s+', ' ', cleaned_data)
    return cleaned_data.strip()

if __name__ == "__main__":
    # Пример использования
    input_text = input("Введите текст на русском языке: ")
    result = strip_punctuation_ru(input_text)
    print("Результат обработки:", result)
