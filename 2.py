import sys

def main():
    # Проверяем, есть ли параметры командной строки
    if len(sys.argv) == 1:
        print("NO PARAMS")
        return

    try:
        # Инициализируем переменные для суммы и коэффициента
        total = 0
        sign = 1

        # Проходимся по аргументам командной строки, начиная с индекса 1
        for arg in sys.argv[1:]:
            # Пробуем преобразовать аргумент в целое число
            num = int(arg)
            # Увеличиваем сумму на число, умноженное на текущий знак
            total += sign * num
            sign *= -1

        # Выводим общую сумму
        print(total)
    except ValueError:
        # Если возникает ошибка преобразования типов
        print("ValueError")
    except Exception as e:
        # Выводим имя класса исключения в случае другой ошибки
        print(e.__class__.__name__)

if __name__ == "__main__":
    main()

