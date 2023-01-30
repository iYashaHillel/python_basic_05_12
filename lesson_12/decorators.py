import time


def hello_decorator(call_times):
    def wrapper(func):
        def inner(*args, **kwargs):
            print("Hello, this is before function execution")
            for _ in range(call_times):
                result = func(*args, **kwargs)
            print("This is after function execution")
            return result

        return inner
    return wrapper


@hello_decorator(call_times=3)
def greetings(name: str, age: int, a):
    return f'Hello {name}'


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


res = func_1(10000000)
res = func_2(10000000)
print(res)
