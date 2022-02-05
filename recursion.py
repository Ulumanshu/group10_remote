import sys


def recursive_func(number):
    if number != 0:
        print(number)
        number = recursive_func(number - 1)

    return number


if __name__ == '__main__':
    sys.setrecursionlimit(11000)
    recursive_func(9)
