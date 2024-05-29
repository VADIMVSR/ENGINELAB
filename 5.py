import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        return None

def print_file_content(lines, add_num=False, add_count=False, sort_lines=False):
    if lines is None:
        print("ERROR")
        return

    if sort_lines:
        lines.sort()

    if add_num:
        for i, line in enumerate(lines):
            print(f"{i} {line.strip()}")
    else:
        for line in lines:
            print(line.strip())

    if add_count:
        print(f"rows count: {len(lines)}")

def main():
    # Проверяем, что количество аргументов не менее 2 (имя скрипта и имя файла)
    if len(sys.argv) < 2:
        print("ERROR")
        return

    # Извлекаем имя файла из аргументов командной строки
    filename = sys.argv[-1]

    # Проверяем существование файла
    lines = read_file(filename)

    # Обработка дополнительных аргументов
    add_num = '--num' in sys.argv
    add_count = '--count' in sys.argv
    sort_lines = '--sort' in sys.argv

    # Вывод содержимого файла
    print_file_content(lines, add_num, add_count, sort_lines)

if __name__ == "__main__":
    main()

