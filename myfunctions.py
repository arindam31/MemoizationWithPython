import memoize
import timeit

"""
This python file contains few "expensive" functions in terms of time.
"""


def add(a,b):
    return a + b

def fibonacci(num):
    if num <= 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)

memoize_fib = memoize.memoize(fibonacci)
memoize_fact = memoize.memoize(factorial)

if __name__ == '__main__':
    # Without Memoization
    # 1st SET
    print '---------------- First calculation 1st Set Direct function call ---------------------'
    print timeit.timeit('fibonacci(7)', setup='from __main__ import fibonacci', number=1)
    print timeit.timeit('factorial(5)', setup='from __main__ import factorial', number=1)

    print '---------------- First calculation With Memoization 1st Set ---------------------'
    print timeit.timeit('memoize_fib(7)', setup='from __main__ import memoize_fib', number=1)
    print timeit.timeit('memoize_fact(5)', setup='from __main__ import memoize_fact', number=1)


    # Below two statements should show almost same time as above.
    # 1st Set Repeat
    print '----------------------1st Set Repeat-----------------------------'
    print timeit.timeit('memoize_fib(7)', setup='from __main__ import memoize_fib', number=1)
    print timeit.timeit('memoize_fact(5)', setup='from __main__ import memoize_fact', number=1)


    # 2nd Set
    print '-----------------First calculation 2nd Set-----------------------'
    print timeit.timeit('memoize_fib(5)', setup='from __main__ import memoize_fib', number=1)
    print timeit.timeit('memoize_fact(8)', setup='from __main__ import memoize_fact', number=1)

    # This set calculation must begin to show improvement
    # 1st Set repeat
    print '-------------------Recalculating 1st set--------------------------'
    print timeit.timeit('memoize_fib(7)', setup='from __main__ import memoize_fib', number=1)
    print timeit.timeit('memoize_fact(5)', setup='from __main__ import memoize_fact', number=1)

    # This set calculation must begin to show improvement
    # 2nd Set repeat
    print '-------------------Recalculating 2nd set--------------------------'
    print timeit.timeit('memoize_fib(5)', setup='from __main__ import memoize_fib', number=1)
    print timeit.timeit('memoize_fact(8)', setup='from __main__ import memoize_fact', number=1)


