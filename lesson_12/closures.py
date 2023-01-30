"""
Замыкание (closure) представляет функцию, которая запоминает свое
лексическое окружение даже в том случае, когда она выполняется вне
своей области видимости.
"""


# def outer_func(name):
#     leader = name
#
#     def print_leader():
#         print(leader)
#
#     return print_leader
#
#
# f = outer_func('Ivan')
# del outer_func
#
# f()
#
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

