import json
from typing import Callable, List, Dict, Optional
import os

# contacts = [
#     {
#         'name': 'John',
#         'phone_number': '+3806671123123'
#     },
#     {
#         'name': 'Maria',
#         'phone_number': '+3809555555555'
#     },
#     None,
#     True,
#     False,
#     2.5,
#     (1, 2, 3, 4, 5)
# ]
# JSON, Pickle
# CSV
# name, phone_number
# John, +3806671123123
# Maria, +3809555555555

# with open('contacts.txt', 'w') as f:
#     f.write(json.dumps(contacts))


# with open('contacts.txt', 'r') as f:
#     string_data = f.read()
#     data = json.loads(string_data)

# print(data)


contacts: List[Dict[str, any]] = []


def get_menu() -> str:
    return '0 - Contacts list\n' \
           '1 - Add contact\n' \
           '2 - Edit contact\n' \
           '3 - Delete contact\n' \
           '4 - Exit\n> '


def infinity_input(
    message: str,
    validator: Optional[Callable[[str], bool]] = None,
    return_type: Callable[[any], any] = str,
) -> any:
    while True:
        value = input(message)
        if not value or (validator is not None and not validator(value)):
            print('Wrong value')
            continue
        return return_type(value)



def add_contact() -> None:
    name = infinity_input('Enter name: ', lambda x: x.isalpha())
    phone_number = infinity_input('Enter phone number: ')
    contact = {
        'name': name,
        'phone_number': phone_number
    }
    contacts.append(contact)


def edit_contact(contact_id: int) -> None:
    name = infinity_input('Enter name: ')
    phone_number = infinity_input('Enter phone number: ')
    contacts[contact_id] = {
        'name': name,
        'phone_number': phone_number
    }


def print_contacts() -> None:
    for i, contact in enumerate(contacts):
        print(f'{i} - {contact}')


def delete_contact(contact_id: int) -> None:
    contacts.pop(contact_id)


def load_contacts() -> None:
    global contacts
    try:
        with open('contacts.json', 'r') as f:
            contacts = json.loads(f.read())
    except FileNotFoundError:
        pass
    print(f'Loaded {len(contacts)} contacts')


def save_contacts() -> None:
    with open('contacts.json', 'w') as f:
        f.write(json.dumps(contacts))
    print(f'Saved {len(contacts)} contacts')


def run():
    load_contacts()
    menu = get_menu()
    while True:
        choice = infinity_input(menu, lambda x: x in ('0', '1', '2', '3', '4'))
        os.system('clear')
        if choice == '4':
            save_contacts()
            break
        if choice == '0':
            print_contacts()
        if choice == '1':
            add_contact()
        elif choice == '2':
            contact_id = infinity_input(
                'Enter contact id: ',
                lambda x: x.isdigit() and 0 <= int(x) < len(contacts),
                int,
            )
            edit_contact(contact_id)
        elif choice == '3':
            contact_id = infinity_input(
                'Enter contact id: ',
                lambda x: x.isdigit() and 0 <= int(x) < len(contacts),
                int
            )
            delete_contact(contact_id)



# if __name__ == '__main__':
#     try:
#         run()
#     except KeyboardInterrupt:
#         save_contacts()


import pickle


# with open('data.bin', 'wb') as f:
#     data = pickle.dumps({'key': 'value'})
#     f.write(data)

# with open('data_2.bin', 'wb') as f:
#     pickle.dump({'key1': 'value1'}, f)


# with open('data.bin', 'rb') as f:
#     data = pickle.loads(f.read())

# with open('data_2.bin', 'rb') as f:
#     data = pickle.load(f)


# print(abs(-1))
# print(abs(1))

# my_list = [True, False, True, True]
#
# print(all(my_list))  # and
# print(any(my_list))  # or

# print(bin(10))
# print(hex(16))

# print('Hello')
# breakpoint()
# print('World')


def is_func(func):
    if callable(func):
        print('This is function')
    else:
        print('Not a function')


# is_func(print)
# is_func(4)
# print(callable(2))
# print(callable(False))
# print(callable(is_func))

# for i in range(255):
#     print(f'{i} - {chr(i)}')
#
# print(chr(65))
# print(ord('A'))

# my_list = ['Test', 'Test 2', 'Hello', 'world']
#
# for i in range(len(my_list)):
#     print(f'{i} - {my_list[i]}')
#
#
# for i, value in enumerate(my_list):
#     print(f'{i} - {value}')

# print('start execution')
# code = input('Enter code: ')
# print(exec(code))
# print(eval('2 + 2'))
# print('end execution')

# print(globals())
# print(locals())


# iter_list = iter(my_list)
# print(next(iter_list))
#
# if my_list:
#     first_item = my_list[0]
#
# first_item = next(iter(my_list), None)

# import math
#
#
# number = 2.123124124124124
# print(round(2.6))
# print(math.ceil(2.1))
# print(math.floor(2.9))

my_list = ['test', 1, 2, 3, 4]

print(dict(zip(['key', 'key2', 'key3', 'key4', 'key5', 'key6'], my_list)))


