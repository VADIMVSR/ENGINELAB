class DefaultList(list):
    def __init__(self, default_value):
        self.default_value = default_value
        super().__init__()

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default_value

# Пример использования
my_list = DefaultList(default_value="N/A")
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list[0])  # Выведет: 1
print(my_list[2])  # Выведет: 3
print(my_list[5])  # Выведет: N/A, так как индекс 5 выходит за границы списка