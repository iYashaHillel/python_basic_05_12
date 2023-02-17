
class Person:
    country = 'Ukraine'

    def __init__(self, name: str, age: int):
        self.first_name = name
        self.age = age
        self.hello_counter = 0

    def say_hello(self):
        print(hex(id(self)))
        print(f'Hello! My name is {self.first_name}')
        self.hello_counter += 1


person_1 = Person('Tom', 24)
person_2 = Person('Bob', 25)

person_1.city = 'Kiev'

# print(Person.country, Person.city)
print(person_1.country, person_1.city)
# print(person_2.country, person_2.city)
