class Cell:
    def __init__(self, nums):
        self.nums = nums  # 13

    def make_order(self, rows):  # 5
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Sum of cell is: {self.nums + other.nums}'

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше равно второй, вычитание невозможно!"

    def __mul__(self, other):
        return f'Multiply of cells is: {self.nums * other.nums}'

    def __floordiv__(self, other):
        return f'Truediv of cells is: {self.nums // other.nums}'


cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))