

def foo(numbers):
    numbers.append(10)
    print(hex(id(numbers)))


def sample(number = None):
    if number is None:
        number = 0
    if number > 5:
        return number
    number += 1
    res = sample(number)
    return res


# A = []
# foo(A)
# print(hex(id(A)))
# print(A)
# print(sample())


def factorial(x):
    """
    This is a recursive function
    to find the factorial of an integer
    Example:
    1! = 1
    2! = 2 * 1 = 2
    3! = 3 * 2 * 1 = 6
    O(6!) = 6 * 5 * 4 * 3 * 2 * 1
    ...
    """

    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


# res = factorial(200)
# print(res)


# my_list = [1, 21, 3, 43, 4]


# for x in range(10):  # O(N^3)
#     for y in range(10):
#         for j in range(10):
#             print(f'{x} * {y} = {x * y} | {j}')


# my_number = 0

# my_list.insert(0, 5)
#
# for number in my_list:  # O(N)
#     print(number, my_list.count(number))

# print(my_list[2])
#
# my_dict = {
#     'key': 'value',
#     'key2': 'value2'
# }
# print(my_dict['key2'])

