"""
Замыкание (closure) представляет функцию, которая запоминает свое
лексическое окружение даже в том случае, когда она выполняется вне
своей области видимости.
"""
from typing import Union


def outer_func(name):
    leader = name
    print('outer_func')

    def print_leader():
        print('[print_leader] Hello world')
        print(leader)

    return print_leader


f = outer_func('Ivan')
print('-------')
# f.__closure__
# outer_func.data = 'Hello world'
f()
# print(outer_func.data)

def calculator(a: Union[int, float, str, bool], b: Union[int, float, str, bool], func):
    if isinstance(a, str):
        if a.isdigit():
            a = float(a)
        else:
            print('Error a not a number')
            return
    if isinstance(b, str) and b.isdigit():
        if b.isdigit():
            b = float(b)
        else:
            print('Error b not a number')
            return

    a = float(a)
    b = float(b)

    print(func(a, b))


def multiply(a: float, b: float) -> float:
    return a * b


def plus(a: float, b: float) -> float:
    return a + b


# calculator('2123', 3, plus)


def my_map(func, iterable):
    return [func(x) for x in iterable]



# numbers = [1, 2, 3, 4, 5]
# [значение for переменная_цикла in итериуемый_обьект if условие]
# [значение for переменная_цикла in итериуемый_обьект]
# print([x + 1 for x in numbers])
# print(my_map(lambda x: x + 1, numbers))
# print(list(map(int, numbers)))


# new_print = print
#
# print('Test')
# new_print('John')

# del outer_func

# f()

# outer_func('Ivan')


# def outer_func():
#     leader = 'John'
#
#     def print_leader():
#         print(leader)
#
#     return print_leader
#
#
# f = outer_func()
# print(outer_func.__closure__)
# # None
# print(f.__closure__)
# # (<cell at 0x7f6465878070: str object at 0x7f64657afd70>,)
# print(f.__closure__[0].cell_contents)

