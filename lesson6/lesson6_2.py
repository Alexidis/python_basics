class Road:
    """
    Класс Дорога
    """
    def __init__(self, length, wight, height=5):
        """
        Конструктор
        :param length: длина дороги в метрах
        :param wight: ширина дороги в метрах
        :param height: высота асфальта в сантиметрах
        """
        self._length = length
        self._wight = wight
        self._height = height

    def calc_asphalt_mass(self, asphalt_mass):
        """
        метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна
        :param asphalt_mass: масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
        :return: массу асфальта, необходимого для покрытия всего дорожного полотна
        """
        return self._length * self._wight *  self._height * asphalt_mass