# import string
# import random
#
# len_password = 12
# new_password = random.sample(
#     string.digits,
#     k=len_password
# )
# password = ''
# for char in new_password:
#     password += char
# print(password)

# import copy
#
# a = [1, [1, 2], 2, 3]
# b = copy.deepcopy(a)
#
# print(hex(id(a[1])), hex(id(b[1])))
# print(a[1] is b[1])
#
# print(a, b)
# a[1].append(5)
# print(a, b)

# import sys
#
# A = [1, 2, 3]
# A.append(A)
# print(sys.getrefcount(A))
# del A

# SyntaxError
# NameError
# TypeError
# ZeroDivisionError
# ValueError
# IndexError

# try:
#     a = int(input('Enter your number: '))
#     b = int(input('Enter your number: '))
#
#     # print([1, 2][100])
#
#     print(a / b)
# except ValueError as e:
#     print(f'Error! Your value is not a number! System text: {e}')
# except ZeroDivisionError as e:
#     print(f'Error! b is 0! System text: {e}')
# except Exception as e:
#     print(f'Unknown error! System text: {e}')
# else:
#     print('No error found!')
#
# print(f'A = {a} & B = {b}')
# print('end')


# a = input('Enter your number: ')
# if not a.isdigit():
#     raise ValueError(f'{a} is not a number!')
#
# print('OK')


# while True:
#     try:
#         a = int(input('Enter your number: '))
#     except ValueError:
#         print('A is not a number')
#     else:
#         break
#
# print(a)


