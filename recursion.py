import sys


def recursive_func(number, count):
    count = count
    if number != 0:
        print(number, count)
        number = recursive_func(number, count + 1)

    return number


if __name__ == '__main__':
    sys.setrecursionlimit(12000)
    recursive_func(9, 0)
