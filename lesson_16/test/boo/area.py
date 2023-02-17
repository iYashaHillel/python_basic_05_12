from foo import decorators


@decorators.cache_decorator
def triangle_area(a: float, b: float) -> float:
    """
    Функция считает площадь треугольника
    :param a: Сторона треугольника
    :param b: Сторона треугольника
    :return: Площадь
    """

    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    return a * b


@decorators.cache_decorator
def circle_area(r: float) -> float:
    """
    Функция считает площадь круга
    :param r: Радиус
    :return: Площадь
    """

    print(f'Вызвана функция circle_area с аргументом {r}')
    return 3.14 * (r * r)