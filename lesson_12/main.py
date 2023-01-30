from typing import Tuple, List


def get_user_data() -> Tuple[str, str]:
    name = input('Enter your name: ')
    phone_number = input('Enter your phone number: ')
    return name, phone_number


# points = [-10, 10, 0, 4]
# user_name, user_phone_number = get_user_data()
# x, y, z, p = points
#
# print(f'x = {x} | y = {y} | z = {z}')
# print(f'{user_name} | {user_phone_number}')

# documents = ['test.jpg', 'important.pdf', 'holidays.mp4', 1, 2, 3, 'game.exe']
#
# first_item, *other_items = documents
#
# print(first_item, other_items,)
# print(documents)

# names = []
#
# for _ in range(10):
#     name = input('Enter your name: ')
#     if not name:
#         continue
#     names.append(name)


# operation_type, *items, terminal_output = ['+', 1, 2, 3, 4, 5, True]
#
# print(operation_type, items, terminal_output)


def calculator(operation_type: str, *items, terminal_output: bool, **kwargs) -> int:
    summ = 0
    debug_str = ''
    for item in items:
        if operation_type == '+':
            summ += item
            debug_str += f'{item} + '
        elif operation_type == '-':
            summ -= item
            debug_str += f'{item} - '
    if terminal_output:
        print(summ)
    if kwargs.get('debug'):
        print(debug_str)
    return summ


# numbers = [int(input(f'Enter number #{x}: ')) for x in range(4)]

# print(numbers[:3])
# res = calculator('-', 2, 3, 4, 5, 6,1 ,2, 3, 4, 5, 6, 7, 78, 8, terminal_output=True, debug='YES')
# print(res)

# filter, map, sorted, max
# join, split

import random

# numbers = [None, None, None, 1, None, -9, None, -8, None, None, None, 15, -5, 12, 20, None, None, -8, -8, -1]  # [random.randint(-10, 20) if random.randint(0, 1) else None for _ in range(20)]
#
# filtered_numbers = list(filter(lambda x: x is not None and x >= 0, numbers))  # [x for x in numbers if x is not None]

# numbers = ['123', 'asd', '5', '6', 'fg']  # [input(f'Enter number #{x}: ') for x in range(5)]
# numbers_only = filter(lambda x: x.isdigit(), numbers)
# integer_numbers = list(map(lambda x: int(x) + 10, numbers_only))  # [int(x) for x in numbers_only]

# print(numbers)
# print(numbers_only)
# print(sorted(integer_numbers))
# print(max(integer_numbers))


# users = [
#     {
#         'name': 'Petr',
#         'age': 30,
#     },
#     {
#         'name': 'Maria',
#         'age': 20,
#     },
#     {
#         'name': 'John',
#         'age': 25,
#     },
#     {
#         'name': 'Vasya',
#         'age': 50,
#     },
# ]

# print(sorted(users, key=lambda x: x['age'], reverse=False))
# print(max(users, key=lambda x: x['age']))
# print(min(users, key=lambda x: x['age']))

# print(users)



# def foo():
#     x = 2
#     print(f'[foo] X = {x}')
#
# for i in range(5):
#     print(i)
#
# foo()
# print(i)


def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 3

        def func_inner_inner():
            nonlocal x
            x = 4
            print(f'func_inner_inner x = {x}')

        func_inner_inner()
        x = 5
        print(x)

    func_inner()
    print(f'Outer x = {x}')


func_outer()
