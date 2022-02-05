import sys


def recursive_func(number, count):
    count = count
    if number != 0:
        print(number, count)
        number = recursive_func(number - 1, count + 1)

    return number


def factorial_recursive(n):
    """Calculates factorial.

    Args:
        n: the natural number that is the input for the algorithm.
    Returns:
        factorial of number n.
    """
    if n == 0:
        return 1
    else:
        res = n * factorial_recursive(n-1)
        # print(res)
        return res


def factorial_iterative(n):
    """Calculates factorial in an iterative manner.

    Args:
        n: the natural number that is the input for the algorithm.
    Returns:
        factorial of number n.
    """
    result = 1
    for i in range(1, n+1):
        result *= i
        print(i, result)
    return result


if __name__ == '__main__':
    sys.setrecursionlimit(12000)
    recursive_func(9, 0)
    factorial_5 = factorial_recursive(5)
    # print(factorial_5)
    factorial_6 = factorial_iterative(6)
    print(factorial_6)
