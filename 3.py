import sys

def main():
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        operator = sys.argv[3]

        operators = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: x / y if y != 0 else print("Division by zero"),
                     '^': lambda x, y: x ** y}

        result = operators.get(operator, lambda x, y: print("Оператор не поддерживается"))(num1, num2)
        if result is not None:
            print(result)
    except (ValueError, IndexError):
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Много аргументов")
    else:
        main()
