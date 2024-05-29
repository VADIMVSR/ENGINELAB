import string

def is_palindrome(data):
    # Удаляем пробелы и приводим к нижнему регистру
    data = ''.join(c.lower() for c in data if c.isalnum())
    return data == data[::-1]

def main():
    # Считываем строку из стандартного ввода
    user_input = input("Введите строку: ")

    # Проверяем, является ли строка палиндромом
    if is_palindrome(user_input):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
