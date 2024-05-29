def arithmetic_operation(operation):
    if operation == chr(43):#+
        return lambda x, y: x + y
    elif operation == chr(45):#-
        return lambda x, y: x - y
    elif operation == chr(47):#/
        return lambda x, y: x / y
    elif operation == chr(42):#*
        return lambda x, y: x * y
print("Введите операцию\t")
op=str(input())
print("\nВведите первое число\t")
a=float(input())
print("\nВведите второе число\t")
b=float(input())
answer = arithmetic_operation(op)
print("\nОтвет:","{:.7f}".format(answer(a,b)))
