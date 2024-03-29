

def number_generator():
    number = 0
    while number < 5:
        number += 1
        yield number
    print('end generator')


# print(list(range(0, 10)))
# print(list(number_generator()))
# for number in range(0, 10):
#     print(number)


# gen = number_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(gen)


def xrange(n):
    i = 0
    while i < n:
        yield i
        i += 1


# gen = xrange(3)
# print(next(gen))
# print(next(gen))
# print(next(gen))



# for i in list(range(1000000)):
#     print(i)




# for number in xrange(10):  # O(N)
#     print(number)
#
#
# for i in range(10):  # O(N^2)
#     for j in range(10):
#         print(i, j)
#

# numbers = [1, 2, 3, 3, 3, 4, 5, 6]
#
#
# for number in numbers:  # O(N^2)
#     numbers.count(number)  # O(N)

# for i in range(10):  # O(N^3)
#     for j in range(10):
#         for k in range(10):
#             print(numbers[i])


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for y in range(len(matrix)):
#     for x in range(len(matrix[y])):
#         print(matrix[y][x])
# next(d)
# next(d)
# next(d)
# next(d)
# next(d)
# next(d)
# next(d)
# next(d)
# numbers = iter([1, 2, 3, 4, 5, 6])
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))


