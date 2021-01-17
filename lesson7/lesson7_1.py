class Matrix:
    """Коасс Матрица """
    def __init__(self, data):
        """
        Конструктор на основе данных
        :param data: массив данных
        """
        self.rows = [i for i in data]
        self.row_num = len(self.rows)
        self.col_num = len(self.rows[0])
        self.symmetrical = min(len(i) for i in data) == max(len(i) for i in data)

    def __str__(self):
        """
        Перегрузка для преоразования в строку
        :return: возвращает матрицу в текстовом предствлении
        """
        str_row = ''
        for row in self.rows:
            str_row += ''.join(str(row)) + '\n'
        return str_row

    def eq_dimension(self, matrix):
        """
        Проверка размерности матриц
        :param matrix:
        :return:
        """
        both_symmetrical = self.symmetrical and matrix.symmetrical
        same_dimension = (self.row_num, self.col_num) == (matrix.row_num, matrix.col_num)
        return both_symmetrical and same_dimension

    def __add__(self, right_term):
        """
        Сложение матриц
        :param right_term: правое слагаемое
        :return: результат сложения
        """
        # проверяем тип правого слогаемого и размерности матриц
        # тут мог быть try, но не хочу создавать свое исключение для одноразового использования не хочу
        if isinstance(right_term, Matrix) and self.eq_dimension(right_term):
            result_matrix = []
            # т.к. матрицы семетричны и одинаковой размерности, то разницы нет пао какому объекту смотрим
            for row_num in range(self.row_num):
                # собираем строку
                res_row = [self.rows[row_num][col_num] + right_term.rows[row_num][col_num] for col_num in range(self.col_num)]
                # добавляем полученную строку в массив
                result_matrix.append(res_row)
            # возвращаем результпт в типе который операндов
            return Matrix(result_matrix)
        elif not isinstance(right_term, Matrix):
            raise TypeError
        elif not (self.symmetrical and right_term.symmetrical):
            raise Exception('Матрицы не семетричны')
        else:
            raise Exception('Матрицы разных размерностей ')
