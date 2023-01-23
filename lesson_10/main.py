# """
# File main.py Comment
# """
#
# a = int(input('Enter a number #1: '))
# b = int(input('Enter a number #2: '))
# summ = a + b
# for i in range(summ):
#     print(i)
#
# print('end')
#
#
# my_list = []
#
# for i in range(5):
#     user_number = int(input('Enter a number: '))
#     my_list.append(user_number)
#
# print(my_list)
#
# my_list = []
# for x in range(10):
#     if x % 2 == 0:
#         my_list.append(x)
#
# def validate_user_number():
#     number = int(input('Enter a number: '))
#     if number % 2 == 0:
#         return number
#     return 0
#
# my_list = [int(input('Enter a number: ')) for x in range(5)]
# old_matrix = []
# for y in range(3):
#     old_matrix.append([])
#     for x in range(3):
#         old_matrix[y].append(x + y)
#
# print(old_matrix)
# matrix = [[x + y for x in range(3)] for y in range(3)]
# print(matrix)
#
# list, set, dict
# int
#
# a = 4
# print(hex(id(a)))
#
# a = 'hello'
# print(hex(id(a)))
#
# print( (2 + 2) * 2 )
#
# my_tuple = 1, [1, 2, 3], 3, 4, 'str', 2.5, True
#
# print(my_tuple)
# # my_tuple[1] += [4, 5]
# my_tuple[1].extend([4, 5])
# print(my_tuple)

# my_list = [x for x in range(10)]
#
# my_tuple = tuple(my_list)
# my_new_list = list(my_tuple)
# print(my_tuple)

# my_set = {1, 2, 3, 4, 5, 6, 7}
# my_set_2 = {'Hello', 'world'}
#
# my_set.add(10)
# my_set.update(my_set_2)
#
#
# print(my_set)
# for item in my_set:
#     print(item)
# 1, 2, 3, 4.. 30
# 31, 32, 33
# 61, 62
# print(61 % 40)
# print(hash('hello'))
# print(hash('hello') % 30)
# print(chr(66))
# print(ord('A'))
# print(hash(123))
# print(my_set[0])
# print(my_set, type(my_set))
# print(hash([1, 2, 3]))
# print(hash('hello1'))

# A = {1, 2, 3, 4, 5}
# B = {5, 6, 7, 8, 9}

# new_set = A | B  # A.union(B)  # A.update(B)  # A |= B
# new_set = A & B  # A.intersection(B)  # A.intersection_update(B)  # A &= B
# new_set = B - A  # A.difference(B)  # A.difference_update(B)  # A -= B
# new_set = A ^ B  # A.symmetric_difference(B)  # A.symmetric_difference_update(B)  # A ^= B
