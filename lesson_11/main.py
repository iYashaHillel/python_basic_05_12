from typing import Union, Optional
import random

# a = {1, 2, 3}
# frozen_a = frozenset({1, 2, 3})
# a.add(frozen_a)
#
# print(a, frozen_a)
# print(hash(frozen_a))

# users = [
#     ['Petr', '+380999999999', 30],
#     ['John', '+112312412541', 25],
# ]
#
# print(users[1][1])

user = {
    'age': 30,
    'name': 'John',
    'phone_number': '+112312412541',

    'numbers': [1, 2, 3, 4],
    1: True,
    frozenset((1, 2, 3)): 'Test'
}
address = {
    'country': 'Ukraine',
    'city': 'Kiev',
    'street': '...'
}
# print(user)
# del user[1]
# user.pop(1)
# try:
#     user['asdasd']
# except KeyError:
#     print('Key not found')
# print(user.get('numbers', 'not found'))
# print(user.get('123124'))
# print(user.keys())
# print(user.values())
# for key, value in user.items():
#     print(key, value)
# print(user.pop('numbers', 1231))
# print(user.popitem())
# print(user.popitem())
# user.update()
# user['country'] = address['country']
# user['city'] = address['city']
# user.update(address)
# user['address'] = address
# user.update({'key': 'value1', 'name': 'Petr'})
# new_dict = user.fromkeys(['key1', 'key2', 'key3'], None)
# print(user)
# print(new_dict)
# import copy
#
# new_user = copy.deepcopy(user)
# new_user['name'] = 'Petr'
#
# new_user['numbers'].append(5)
# print('OLD USER', user)
# print('NEW USER', new_user)
# print(hex(id(user)), hex(id(new_user)))

# print(user)
#
# print(user.setdefault('123123', 'Petr'))
#
# print(user)

# print(len(user))


def create_user():
    name = input('Enter name: ')
    phone_number = input('Enter phone number: ')
    age = input('Enter age: ')
    if not (age.isdigit() and name and phone_number):
        print('Error!')
        return None
    age = int(age)
    if age < 0:
        print('Age error!')
        return None
    return {
        'name': name,
        'phone_number': phone_number,
        'age': age
    }


def get_max_number(a: Union[int, float], b: Union[int, float]) -> float:
    print(f'a = {a}, b = {b}')
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('a or b must be int or float')
    if a > b:
        return float(a)
    return float(b)



# print(get_max_number(3.5, b=2))
# create_user()
# while not (user := create_user()):
#     print('Try again')
# print(user)
# print(f'Hello {user["name"]}')


def foo():
    pass


def print_user(name: str, age: int, phone_number: Optional[str] = 'Hello') -> None:
    print(f'Name: {name}')
    print(f'Age: {age}')
    if phone_number:
        print(f'Phone number: {phone_number}')


# print_user('John', phone_number='asdasd', age=30)


# get_int = lambda from_int, to_int: random.randint(from_int, to_int)
#
# print(get_int(1, 10))
# print(get_int(1, 10))

# filter, map, reduce, sorted

numbers = [10, 23, 44, -1, 2, 4]

filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
print(tuple(filtered_numbers))

