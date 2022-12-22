
# text = 'Hello world'
# csv
# name, age, address
# Petr, 25, Kiev
# Vasya, 30, Odesa


# new_text = text.replace('l', '@').replace('o', '_')
# print(text, new_text)
# print(csv_value_1.split(', '))

# text = 'hEllO woRlD'

# print(text.upper())
# print(text.lower())
# print(text.casefold())
# print(text.title())
# print(text.capitalize())
# print(text.swapcase())

# text = '___Hello world____'
#
# print(text.lstrip('_'))
# print(text.rstrip('_'))
# print(text.strip('_'))

# text = 'Hello world'

# print(text.count('l'))
# print('Hello' in text)

# print('14'.zfill(4))
# print('4'.zfill(4))
# print('123456'.zfill(4))

# for i in range(10):
#     for j in range(10):
#         print(f'{i} * {j} = {i * j}')

# print('**'.rjust(5, '#'))


# a = [1, 2, 'Hello', True, 1.5]
# b = (1, 2, 'Hello', True, 1.5)
#
# print(type(a), type(b))
# list

# text = 'Hello world'
#
# print(text[1])  # ello

# a = [1, 2, 'Hello', True, 1.5]

# print(a[::-1])
# print(a)
# a[1] = 'world'
# a[0:4] = [True, False,]
# print(a)

# for i in a:
#     print(i)

# import random
#
# a = []
# for i in range(10):
#     random_number = random.randint(0, 100)
#     # print(a)
#     a.append(random_number)

# print(max(a))
# print(min(a))
# print(a)
# print(sorted(a, reverse=True))
# print(a.sort())
# print(a)
# a.append(-10)
# a.sort(reverse=True)
# print(a)
# print(len(a))
# print(sum(a))

# print(4 in a)

# a = [1, 2, 3, 3, 4, 5, 6]
#
# print(a)
# a.append(-1)
# a.insert(2, -1)
# a.extend([1, 2, True])  # a + [1, 2, True]
# b = a + [1, 2, True]
# a += [1, 2, True]
# a = [1, 2, True] + a
# a.reverse()
# sorted()
# reversed()
# item = a.pop()
# a.remove(3)
# a.remove(3)
# a.reverse()
# print(a.index(60))
# print(a)
# print(a.count(10))

# print(a.copy())
# a.clear()
# print(a)


# text = 4  # 'Hello world'
#
# print(hex(id(text)))
#
# text += 2  # '!'
# print('1')
# print(hex(id(text)))


# a = [1, 2]

# print(hex(id(a)))
# 10 - 4 = 6
# 6 - 7 = -1
# 10 * 2 = 20
# 20 - 11 = 9
# a += [3, 4]

# print(hex(id(a)))

a = [1, 2, 3]
b = a

print(hex(id(a)), hex(id(b)))
print(a, b)
b += [4, 5]
print(hex(id(a)), hex(id(b)))
print(a, b)




