class MyComplex:
    """
    Класс "Комплексное число»"
    """
    def __init__(self, real, img=0):
        self.real = int(real)
        self.img = int(img)

    def __str__(self):
        if self.real and self.img:
            return f'{self.real}+{self.img}j'
        elif not self.real:
            return f'{self.img}j'
        else:
            return f'{self.real}j'

    def __add__(self, other):
        real = self.real + other.real
        img = self.img + other.img
        return MyComplex(real, img)

    def __mul__(self, other):
        real = self.real * other.real - self.img * other.img
        img = self.img * other.real + self.real * other.img
        return MyComplex(real, img)


def main():
    (real, img) = input('Задайте реальную и вещественнуб часть первого числа через пробел ').split(' ')
    a = MyComplex(real, img)
    (real, img) = input('Задайте реальную и вещественнуб часть второго числа через пробел ').split(' ')
    b = MyComplex(real, img)
    c = a + b
    d = a * b
    print(f'Сложение комплексных чисел {a} и {b} равно {c}, а их умножение равно {d}')
