import abc

"""
1) Наследование
2) Полиморфизм
3) Инкапсуляция
4) Абстракция/Интерфейсы
"""
# property .getter .setter .deleter
# Staticmethod
# Classmethod

class ICar(abc.ABC):
    @abc.abstractmethod
    def drive(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def turn(self, direction: str):
        pass



class Car(ICar):
    max_speed = 50

    def __init__(self, brand: str, model: str, color: str, year: int, price: float, vin: str):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        # self.vin = vin  # Public
        # self._vin = None  # Protected
        self.__vin = None  # Private
        self.set_vin(vin)

    def set_vin(self, vin: str) -> None:
        if len(vin) != 10:
            raise ValueError('vin must be 10 symbols')
        self.__vin = vin

    def get_vin(self) -> str:
        return '*' * 8 + self.__vin[-2:]

    def drive(self):
        print(f'[{self.brand} {self.model}] Driving')

    def stop(self):
        print(f'[{self.brand} {self.model}] Stopping')

    def turn(self, direction: str):
        print(f'[{self.brand} {self.model}] Turning {direction}')


# mercedes = Car('Mercedes', 'S500', 'Black', 2019, 100000, '1234567890')
# print(mercedes.get_vin())
# mercedes.set_vin('1234567890')
# print(mercedes.get_vin())
# # print(mercedes.__vin)
# # print(dir(mercedes))
# print(mercedes._Car__vin)


class FlyingCar(ICar):

    def fly(self):
        print(f'[{self.brand} {self.model}] Flying')

    def land(self):
        print(f'[{self.brand} {self.model}] Landing')


class ElectroCar(ICar):

    def __init__(self, brand, model, max_charging_power: float, *args, **kwargs):
        self.brand = brand
        self.model = model
        self.max_charging_power = max_charging_power

    def charge(self):
        print(f'[{self.brand} {self.model}] Charging')

    def drive(self):
        print(f'[{self.brand} {self.model}] Driving silently')

    def stop(self):
       print(f'[{self.brand} {self.model}] Stopping silently')

    def turn(self, direction: str):
        print(f'[{self.brand} {self.model}] Turning {direction} silently')



class Ship(ICar):
    pass



def take_coffee(car: ICar):
    if not isinstance(car, ICar):
        raise TypeError('car must be ICar')
    car.drive()
    car.turn('left')
    car.turn('left')
    car.turn('drive')
    car.stop()


# tesla = ElectroCar('Tesla', 'Model S', 100)
# take_coffee(mercedes)
# take_coffee(tesla)


class A:

    def hello(self):
        print('Hello A')


class B(A):

    def hello(self):
        print('Hello B')


class C(A):

    def hello(self):
        print('Hello C')


class D(B, C):
    pass


# D().hello()
# print(D.__mro__)


class Foo:
    some_attribute = 'some value'

    def __init__(self, name: str):
        self.name = name

    def __del__(self):
        print(f'{self.name} deleted')

    def __str__(self):
        return f'Foo({self.name})'

    def __int__(self):
        return 1

    def __float__(self):
        return 1.0

    def __bool__(self):
        return True

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return Foo(self.name + other.name)

    def __sub__(self, other):
        if isinstance(other, Foo):
            return Foo(f'{self.name} - {other.name}')
        elif isinstance(other, int):
            return Foo(self.name[:-other])

    def hello(self):
        print(f'Hello {self.name}')

    @classmethod
    def print_some_attribute(cls):  # cls - class
        print(cls.some_attribute)

    @staticmethod
    def print_hello():
        print('Hello')

# numpy
a = Foo('John')
b = Foo('Bob')
print(len(a), b)
print(a - 2)
# import time
#
# a = Foo('John')
# a.hello()
# print('------------------')
#
# del a
# for i in range(4):
#     print(i)
#     time.sleep(1)

