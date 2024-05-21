class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range(10)]
        self.sunk_ships = []

    def shoot(self, row, col, result):
        if result == 'sink':
            self.sunk_ships.append((row, col))
        elif result == 'hit':
            self.map[row][col] = 'x'

    def cell(self, row, col):
        if self.map[row][col] == '.':
            for r, c in self.sunk_ships:
                if abs(row - r) <= 1 and abs(col - c) <= 1:
                    return '*'
            return '.'
        return self.map[row][col]

# Пример использования класса SeaMap
sm = SeaMap()
sm.shoot(2, 0, 'sink')
sm.shoot(6, 9, 'hit')

# Вывод карты
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()