import time
from typing import Union, Callable
from typing import List


class Range:
    """ Iterator """

    def __init__(self, from_: int, to_: int):
        self.from_ = from_
        self.to_ = to_
        self.current_ = from_

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_ > self.to_:
            raise StopIteration
        current = self.current_
        self.current_ += 1
        return current


# iterator = Range(0, 2)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in Range(0, 10):
#     print(i)


class TimeIt:
    """ Decorator """

    def __init__(self, func: Callable) -> None:
        self.function = func
        self.results = {}

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.function(*args, **kwargs)
        print(f'{self.function.__name__} - {time.time() - start}s')
        return result


@TimeIt
def pow_numbers(numbers: List[Union[int, float]]) -> float:
    result = .0
    for number in numbers:
        result += number ** number
    return result


# pow_numbers([100, 50])
# pow_numbers([10, 50])
# pow_numbers([100, 50])

# @functools.cache
# def factorial(n):
#     return n * factorial(n-1) if n else 1


class File:
    """ Context manager """

    def __init__(self, file_name: str, mode: str) -> None:
        self.file_obj = open(file_name, mode)

    def __enter__(self):
        print('Open')
        return self.file_obj

    def __exit__(self, *args, **kwargs):
        print('Close')
        print(args, kwargs)
        self.file_obj.close()


class Phone:
    """ Functor """

    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def __call__(self, phone_number: str):
        print(f'{self.phone_number} call {phone_number}')
