"""
Написать декоратор @cache который будет кэшировать входные и выходные данные функции. Для хранения входных и выходных данных нужно использовать словарь. Входные данные обязательно должны быть immutable типами. Важно что для каждой декорируемой функции должен быть свой словарь.

Пример:
Вызывается функция triangle_area с параметрами a=5, b=10
Мы проверяем в словаре что ранее эта функция вызывалась с такими параметрами, если нет, то вызываем функцию triangle_area внутри декоратора и сохраняем в словарь параметры с которыми она вызывалась и результат который вернула и возвращаем результат из декоратора.

Снова вызывается функция triangle_area с параметрами a=5, b=10
Мы проверяем в словаре что ранее эта функция вызывалась с такими параметрами, так как у нас ранее были сохранены входные и выходные параметры функции, то мы можем не вызывать triangle_area внутри декоратора, и вернем прошлый результат выполнения этой функции с параметрами a=5, b=10 из декоратора.
"""
# import app
print(f'IN FILE DECORATORS.py: {__name__}')
VERSION = '0.1.0'

def cache_decorator(func):
    cache = {}

    def inner(*args, **kwargs):
        cache_key = args + tuple(kwargs.values())
        if cache_key in cache:
            return cache[cache_key]
        res = func(*args, **kwargs)
        cache[cache_key] = res
        return res

    return inner


if __name__ == '__main__':
    print('TEST')
    print('test 2')
