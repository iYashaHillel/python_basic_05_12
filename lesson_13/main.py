"""
Программа запрашивает у пользователя пароль и записывает в переменную password.

Необходимо посчитать сложность пароля, где за каждую пройденную проверку пароль получает +1 балл к итоговой оценке, максимальное количество баллов - 5

Проверки:

Длина пароля больше или равно 8 символам
В пароле есть хотя бы одна цифра
В пароле есть хотя бы одна большая
В пароле есть хотя бы одна маленькая буква
В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)
После всех проверок нужно вывести пользователю число - количество баллов за пароль, а так-же рекомендации по улучшению пароля.
"""
# import string
#
# password = input('Введите пароль: ')
# score = len(password) >= 8
# has_digit = False
# has_upper = False
# has_lower = False
# has_spec = False
#
# for char in password:
#     if char.isdigit():
#         has_digit = True
#     if char.isupper():
#         has_upper = True
#     if char.islower():
#         has_lower = True
#     if char in string.punctuation:
#         has_spec = True
#
# score += has_digit + has_upper + has_lower + has_spec

# NLP

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut gravida lorem. Ut turpis felis, pulvinar a semper sed, adipiscing id dolor. Pellentesque auctor nisi id magna consequat sagittis. Curabitur dapibus enim sit amet elit pharetra tincidunt feugiat nisl imperdiet. Ut convallis libero in urna ultrices accumsan. Donec sed odio eros. Donec viverra mi quis quam pulvinar at malesuada arcu rhoncus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In rutrum accumsan ultricies. Mauris vitae nisi at sem facilisis semper ac in est.'
numbers_str = '123,4,5,62,4,11'

# words = text.split()
# print(len(words))

# numbers = numbers_str.split(',')
# numbers = list(map(int, numbers))
#
# true_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# true_numbers = list(map(str, true_numbers))
# result = '_asdas_'.join(true_numbers)
#
# print(numbers)
# print(true_numbers)
# print(result)

# text = 'Hello_world'
#
# print(text.split(' '))


