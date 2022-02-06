import sys
from functools import wraps  # Koks tikslas naudoti functools wraps - padeda, kai reikia suzinoti apgaubtos funcijos info
from time import time
from string import ascii_lowercase, ascii_uppercase, digits
import random
from pprint import pprint
import json


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


def create_record(index_):
    data_dict = dict()
    data_dict['id'] = index_
    data_dict['name'] = ''.join([ascii_lowercase[random.randint(0, len(ascii_lowercase) - 1)] for i in range(5)])
    data_dict['records'] = list()

    return data_dict


def recursive_update(mega_list, depth=0):
    depth = depth
    if depth <= 3:
        for nr, object_ in enumerate(mega_list):
            # records_ = object_.get('records', []) or []
            collected = []
            for i in range(2 * 6 - depth):
                max_list_index = len(mega_list) - 1
                random_idx_ = random.randint(0, max_list_index)
                random_obj_ = dict(mega_list[random_idx_])
                r_obj_id = random_obj_.get('id')
                collected.append(create_record(r_obj_id))

            object_['records'] = list(collected)
            # records_ = object_['records']
            # print(depth, object_['id'])
            # pprint(object_)
            if object_['records']:
                records_ = recursive_update(object_['records'], depth + 1)

            if depth == 0:
                print(nr, len(mega_list))

    return mega_list


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

    object_list = []
    for e in range(100):
        rec = create_record(e)
        object_list.append(rec)

    # pprint(object_list)
    object_list = recursive_update(object_list)
    # pprint(object_list)

    with open('homework_recursion.json', 'w') as f:
        # json.dump(object_list, f)
        file_data = json.dumps(object_list)
        f.write(file_data)
