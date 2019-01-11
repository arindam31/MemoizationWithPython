import memoize
import timeit
import datetime
import time

"""
This python file contains few "expensive" functions in terms of time.
"""
my_memoize_with_args_and_timer = lambda f: memoize.memoize_with_args_and_timer(f, 1)

@memoize.memoize_with_args
def add(*args):
    return sum(args)

@my_memoize_with_args_and_timer
def multiply(*args):
    prod = 1
    for num in args:
        prod *= num
    return prod

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
    # Without Memoization (Factorial and Fibinacci functions)
    # 1st SET

    print '---------------- First calculation 1st Set Direct function call ---------------------'
    print timeit.timeit('fibonacci(7)', setup='from __main__ import fibonacci', number=1)
    print timeit.timeit('factorial(5)', setup='from __main__ import factorial', number=1)


    # Using memoization
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

    # Let's see the cached values
    print 'Factorial Cache'
    print memoize_fact.__closure__[0].cell_contents

    print 'Fibo Cache'
    print memoize_fib.__closure__[0].cell_contents

    print '-------------- Add Function memoized ------'
    print "Cache for add function before calling it.:",add.__closure__[0].cell_contents

    print 'Memoize with multiple arguments example'
    # 1st set first call with memoize
    print add(2,3)
    print add(1,2,3,4,5)
    print "Cache after 1st call:", add.__closure__[0].cell_contents

    # 1st set second call with memoize
    print add(2,3)
    print add(1,2,3,4,5)
    print "Cache after 2nd call:", add.__closure__[0].cell_contents

    print '-------------- Multiply Function memoized with timer check ------'
    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    print multiply(2,3,5)

    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    print multiply(2,3,5)

    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    print multiply(2,3,5)

    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    print multiply(2,3,5)

    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    time.sleep(1) # This is to expire timer.
    print multiply(2,3,5)

    # Should see new expiry time
    print "Cache for multiply:", multiply.__closure__[0].cell_contents
