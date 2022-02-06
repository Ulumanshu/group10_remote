# Python program to display the Fibonacci sequence
from functools import wraps  # Koks tikslas naudoti functools wraps
from time import time


def timing(f):

    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        print("ARGSAI TIMITE: ", args, *args)
        print('KWARGSAI', kw)
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
        return result

    return wrap


# @timing
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


nterms = 100

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       ts = time()
       print(recur_fibo(i))
       te = time()
       print(i)
       print('f%2.4f sec' % (te - ts))
