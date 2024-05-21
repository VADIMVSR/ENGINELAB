def check_password(password):
    # Проверка длины пароля
    if len(password) <= 8:
        return "error"

    # Проверка наличия больших и маленьких букв
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return "error"

    # Проверка наличия хотя бы одной цифры
    if not any(char.isdigit() for char in password):
        return "error"

    # Проверка на комбинации из 3 буквенных символов
    keyboard_layouts = ['qwertyuiop', 'йцукенгшщзхъ', 'asdfghjkl', 'фывапролджэ', 'zxcvbnm', 'ячсмитьбю']
    for layout in keyboard_layouts:
        if layout in password.lower():
            return "error"

    return "ok"

# Пример использования
password = input("Введите пароль: ")
result = check_password(password)
print(result)