"""
#12 и #14
Модули и пакеты
ООП
API
"""


"""
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.

Пример ввода:
3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt
"""

# available_operation = {
#     'read': 'R',
#     'write': 'W',
#     'execute': 'X',
# }
# files = {}
# output = []
# n = int(input('Enter file count: '))
#
# for _ in range(n):
#     file_name, *operation = input('> ').split()
#     files[file_name] = operation
#
# m = int(input('Enter operation count: '))
# for _ in range(m):
#     operation, file_name = input('> ').split()
#     if available_operation[operation] in files[file_name]:
#         output.append('OK')
#     else:
#         output.append('Access denied')
#
# print('\n'.join(output))
from test import decorators as first_decorator
# from foo import decorators as second_decorator
#
# from test.boo.area import triangle_area, circle_area
#
# print(first_decorator.VERSION, second_decorator.VERSION)
#
# print('Результат выполнения triangle_area(5, 10):', triangle_area(a=5, b=10))  # Тело функции выполниться так как функция вызывается в первый раз с такими аргументами
# print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))  # Тело функции не выполниться так как функция ранее вызывалась с такими аргументами
# print('Результат выполнения circle_area(20):', circle_area(20))  # Тело функции выполниться так как функция вызывается в первый раз с такими аргументами
# print('Результат выполнения triangle_area(10, 10):', triangle_area(10, 10))  # Тело функции выполниться так как функция вызывается в первый раз с такими аргументами
# print('Результат выполнения circle_area(20):', circle_area(20))  # Тело функции не выполниться так как функция ранее вызывалась с такими аргументами


# print(f'IN FILE APP.py {__name__}')


