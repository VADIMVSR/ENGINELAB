import sys


def check_password(password):
    try:
        assert len(password) > 8, "Длина пароля должна быть не менее 9 символов"
        assert any(char.isupper() for char in password) and any(
            char.islower() for char in password), "Пароль должен содержать символы верхнего и нижнего регистра"
        assert any(char.isdigit() for char in password), "Пароль должен содержать хотя бы одну цифру"

        keyboard_layouts = ['qwertyuiop', 'йцукенгшщзхъ', 'asdfghjkl', 'фывапролджэ', 'zxcvbnm', 'ячсмитьбю']
        for layout in keyboard_layouts:
            assert layout not in password.lower(), "Пароль не должен содержать последовательность из подряд идущих трех символов"

        return True
    except AssertionError as e:
        print(f"Имя класса исключения: {e.__class__.__name__}")
        return False


while True:
    password = input("Введите пароль: ")
    if password.lower() == "ctrl+break":
        print("Bye-Вуе")
        sys.exit()

    if check_password(password):
        print("ok")
        break