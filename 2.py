class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

class SequenceError(PasswordError):
    pass

def check_password(password):
    if len(password) <= 8:
        raise LengthError("Длина пароля должна быть не менее 9 символов")

    if all(char.isupper() for char in password) or all(char.islower() for char in password):
        raise LetterError("Пароль не должен состоять только из символов одного регистра")

    if not any(char.isdigit() for char in password):
        raise DigitError("Пароль должен содержать хотя бы одну цифру")

    keyboard_layouts = ['qwertyuiop', 'йцукенгшщзхъ', 'asdfghjkl', 'фывапролджэ', 'zxcvbnm', 'ячсмитьбю']
    for layout in keyboard_layouts:
        if layout in password.lower():
            raise SequenceError("Пароль не должен содержать последовательность из подряд идущих трех символов")

    return "ok"

# Пример использования
try:
    password = input("Введите пароль: ")
    result = check_password(password)
    print(result)
except PasswordError as e:
    print(f"Ошибка: {e}")