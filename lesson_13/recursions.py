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


# res = factorial(4)
# print(res)

