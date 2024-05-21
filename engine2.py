def simple_map(trasformation, values,y):
    a = []
    for i in values:
        a.append(trasformation(i,y))
    return a
def arithmetic_operation(operation):
    if operation == chr(43):#+
        return lambda x, y: x + y
    elif operation == chr(45):#-
        return lambda x, y: x - y
    elif operation == chr(47):#/
        return lambda x, y: x / y
    elif operation == chr(42):#*
        return lambda x, y: x * y

ish = []
n=int(input())
for i in range(0,n):
  print(i+1,"Число:")
  ii=int(input())
  ish.append(ii)
print("Изначальный список:\n",ish)
print("Введите операцию\t")
op=str(input())
print("\nВведите число y\t")
y=int(input())
o=arithmetic_operation(op)
print("Результатирующий список:\n",*simple_map(o, ish,y))
