import time


def hello_decorator(func):

    def inner():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    return inner


def timeit(func):

    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start)
        return res

    return inner


@timeit
def greetings(iter_count: int):
    summ = 0
    for i in range(iter_count):
        summ ^= i + summ
    return summ


@timeit
def summ_numbers(a, b):
    d = 0
    for i in range(a * b):
        d += a * b
    return d


result = greetings(200_000)
greetings(100_000)
greetings(5_000)

result_2 = summ_numbers(5_000, 5_000)

print(result, result_2)


# result = greetings('John', 30, 'hello')
# print(result)
# decorator = hello_decorator(greetings)
# decorator()


# start = time.time()
# sum = 0
# for i in range(1000000):
#     # print('Hello')
#     sum += i
#
# print(time.time() - start)


def timeit(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)

            with open(filename, 'a') as f:
                f.write(f'[{func.__name__}] {time.time() - start} seconds\n')

            return result

        return wrapper

    return decorator


@timeit('foo_func.log')
def func_1(count):
    sum = 0
    for i in range(count):
        # print('Hello')
        sum += i
    return sum


@timeit('foo_func.log')
def func_2(count):
    return sum(range(count))


# res = func_1(10000000)
# res = func_2(10000000)
# print(res)
