def count_chars(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def main():
    try:
        input_string = input("Введите строку: ")
        result = count_chars(input_string)
        print("Результат подсчета символов:")
        for char, count in result.items():
            print(f"'{char}': {count}")
    except TypeError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
