import sys


def recursive_func(number, count):
    count = count
    if number != 0:
        print(number, count)
        number = recursive_func(number - 1, count + 1)

    return number


def factorial(n):
    """Calculates factorial.

    Args:
        n: the natural number that is the input for the algorithm.
    Returns:
        factorial of number n.
    """
    if n == 0:
        return 1
    else:
        res = n * factorial(n-1)
        print(res)
        return res


if __name__ == '__main__':
    sys.setrecursionlimit(12000)
    recursive_func(9, 0)
    factorial_5 = factorial(5)
    print(factorial_5)
