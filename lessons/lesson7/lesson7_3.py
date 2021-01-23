class Cell:
    """
    Класс Клетка
    """
    def __init__(self, nucleus_num):
        self.nucleus_num = nucleus_num

    def __add__(self, other):
        """
        Перегрузка сложения
        :param other: вторая клетка
        :return: сумма двух клеток
        """
        if isinstance(other, Cell):
            nucleus_num = int(self.nucleus_num + other.nucleus_num)
            return Cell(nucleus_num)
        else:
            raise TypeError

    def __sub__(self, other):
        """
        Перегрузка вычитания
        :param other: вторая клетка
        :return: разность двух клеток
        """
        if isinstance(other, Cell):
            nucleus_num = int(self.nucleus_num - other.nucleus_num)
            if nucleus_num > 0:
                return Cell(nucleus_num)
            else:
                raise Exception ('Результат меньше нуля, клетки самоуничтожились')
        else:
            raise TypeError

    def __mul__(self, other):
        """
        Перегрузка умножения
        :param other: вторая клетка
        :return: произведение двух клеток
        """
        if isinstance(other, Cell):
            nucleus_num = int(self.nucleus_num * other.nucleus_num)
            return Cell(nucleus_num)
        else:
            raise TypeError

    def __truediv__(self, other):
        """
        Перегрузка деления
        :param other: вторая клетка
        :return: частное двух клеток
        """
        if isinstance(other, Cell):
            nucleus_num = self.nucleus_num // other.nucleus_num
            return Cell(nucleus_num)
        else:
            raise TypeError

    def __str__(self):
        """
        Перегрузка преобразования в строку
        :return: строка с количество ячеек ввиде *
        """
        return '*' * self.nucleus_num

    def make_order(self, nucleus_in_row):
        """
        Биение клетки на ряды
        :param nucleus_in_row: количество ячеек в ряду
        :return: строка с ячееками разбитая на строки
        """
        # преобразуем клетку в массив ячеек
        nucleus = list(str(self))
        # расчитываем сколько будет строк
        row_count = int(self.nucleus_num) // nucleus_in_row + 1
        for row in range(1, row_count):
            # расчитываем позицию конца ряда
            row_end = nucleus_in_row * row + row - 1
            # добавлям символ конца ряда
            nucleus.insert(row_end, '/n')
        return ''.join(nucleus)


def main():
    cell = Cell(7)
    cell2 = Cell(5)
    cell3 = cell + cell2
    print(cell3.make_order(5))

    cell3 = cell - cell2
    print(cell3.make_order(1))

    cell3 = cell * cell2
    print(cell3.make_order(7))

    cell3 = cell / cell2
    print(cell3.make_order(1))
