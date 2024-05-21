import sys

def main():
    # Проверяем, что количество аргументов равно 3
    if len(sys.argv) != 3:
        print(0)
        return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        # Выводим сумму аргументов
        print(num1 + num2)
    except ValueError:
        # Если возникает ошибка преобразования типов
        print(0)

if __name__ == "__main__":
    main()
