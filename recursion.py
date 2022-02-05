import sys
from functools import wraps  # Koks tikslas naudoti functools wraps - padeda, kai reikia suzinoti apgaubtos funcijos info
from time import time


def timing(f):

    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
        return result

    return wrap


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


@timing
def factorial_dynamic(n, memory={0:1, 1:1}):
    """Calculates factorial using dynamic programming.

    Args:
        n: the natural number that is the input for the algorithm.
        memory: the results dictionary will be updated with each function call.
    Returns:
        factorial of number n.
    """
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial_dynamic(n-1)
        return memory[n]


if __name__ == '__main__':
    sys.setrecursionlimit(12000)
    recursive_func(9, 0)
    factorial_5 = factorial_recursive(5)
    # print(factorial_5)
    factorial_6 = factorial_iterative(6)
    # print(factorial_6)

    factorial_11 = factorial_dynamic(110)
    print(factorial_11)
    factorial_11 = factorial_dynamic(110)
    print(factorial_11)

    factorial_12 = factorial_dynamic(120)
    print(factorial_12)

    factorial_12 = factorial_dynamic(120, memory=dict({0: 1, 1: 1}))
    print(factorial_12)


