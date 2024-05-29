import sys

def parse_arguments(arguments):
    parsed_args = []

    # Проходимся по аргументам, начиная с индекса 1, так как нулевой аргумент - название скрипта
    for arg in arguments[1:]:
        # Проверяем наличие символа "=" в аргументе
        if '=' in arg:
            key, value = arg.split('=')
            parsed_args.append((key, value))
        elif arg != '--sort':  # Исключаем опцию --sort из вывода ошибки
            print(f"Invalid argument format: {arg}")

    return parsed_args

def print_arguments(parsed_args):
    # Если передана опция --sort, сортируем аргументы по ключу
    if '--sort' in sys.argv:
        parsed_args.sort(key=lambda x: x[0])

    # Выводим отформатированные аргументы
    for key, value in parsed_args:
        print(f"Key: {key} Value: {value}")

def main():
    arguments = sys.argv
    parsed_args = parse_arguments(arguments)
    print_arguments(parsed_args)

if __name__ == "__main__":
    main()
