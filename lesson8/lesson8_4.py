from abc import ABC, abstractmethod


class OfficeEquipment(ABC):

    def __init__(self, brand, model, price):
        """
        Конструктор для пеопределения в дочерних классах
        :param brand: Марка
        :param model: Модель
        :param price: Цена
        """

        self._brand = brand
        self._model = model
        self._price = price
        self._type = ''

    @property
    def type(self):
        return self._type

    @property
    def brand(self):
        return self._brand

    @abstractmethod
    def characteristic(self):
        pass

    @abstractmethod
    def validate(self, *args):
        pass


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, print_speed):
        OfficeEquipment.__init__(self, brand, model, price)
        self._type = 'Принтер'
        if self.validate(brand, model, price, print_speed):
            self._print_speed = print_speed
        else:
            raise Exception(f'Не возможно создать {self._type} с такими параметрами')

    def validate(self, brand, model, price, print_speed):
        return isinstance(brand, str) and isinstance(model, str) and \
               isinstance(price, float) and isinstance(print_speed, int)

    def characteristic(self):
        return f'{self._model} {self._print_speed} {self._price}'


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, scan_speed):
        OfficeEquipment.__init__(self, brand, model, price)
        self._type = 'Сканер'
        if self.validate(brand, model, price, scan_speed):
            self._scan_speed = scan_speed
        else:
            raise Exception(f'Не возможно создать {self.type} с такими параметрами')

    def characteristic(self):
        return f'{self._model} {self._scan_speed} {self._price}'

    def validate(self, brand, model, price, _scan_speed):
        return isinstance(brand, str) and isinstance(model, str) and \
               isinstance(price, float) and isinstance(_scan_speed, int)


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, price, copy_speed):
        OfficeEquipment.__init__(self, brand, model, price)
        self._type = 'Ксерокс'
        if self.validate(brand, model, price, copy_speed):
            self._copy_speed = copy_speed
        else:
            raise Exception(f'Не возможно создать {self._type} с такими параметрами')

    def characteristic(self):
        return f'{self._model} {self._copy_speed} {self._price}'

    def validate(self, brand, model, price, _copy_speed):
        return isinstance(brand, str) and isinstance(model, str) and \
               isinstance(price, float) and isinstance(_copy_speed, int)


class Store:
    def __init__(self):
        self._sku = {}

    def __getitem__(self, item):
        if item not in self._sku.keys():
            self._sku[item] = {'count': 0, 'list': {}}
        return self._sku[item]

    def __setitem__(self, key, value):
        self._sku[key] = value

    @staticmethod
    def get_storage_unit(storage_unit, unit_title):
        return storage_unit.setdefault(unit_title, {'count': 0, 'list': []})

    def accept(self, unit: OfficeEquipment, unit_counts):
        for count in range(unit_counts):
            stock = self[unit.type]
            stock['count'] += 1
            storage_unit = self.get_storage_unit(stock['list'], unit.brand)
            storage_unit['count'] += 1
            storage_unit['list'].append(unit)

    def transfer(self, unit: OfficeEquipment, unit_counts):
        stock = self[unit.type]
        storage_unit = self.get_storage_unit(stock['list'], unit.brand)
        if storage_unit['count'] >= unit_counts:
            for count in range(unit_counts):
                storage_unit['list'].remove(unit)
                storage_unit['count'] -= 1
            stock['count'] -= unit_counts
        else:
            raise Exception('Нежостаточное количество едениц техники на складе')

    def show_remains(self):
        indent = ''
        for u_type, u_type_list in self._sku.items():
            print(f'{indent}{u_type}')
            for brand_name, units in u_type_list['list'].items():
                indent = ' ' * 4
                print(f'{indent}{brand_name}')
                indent = ' ' * 8
                for sku in units['list']:
                    print(f'{indent}{sku.characteristic()}')
            indent = ''
