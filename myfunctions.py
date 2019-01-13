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

@memoize.MemoizeTimer(2)
def sum_of_square(*args):
    _sum = 0
    for num in args:
        _sum += num ** 2
    return _sum

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
    print "Below are timings achieved using various memoization techniques" \
    " Also shown along is cache behaviour and timer expiry"

    print '---------------- Direct function call (fibonacci and factorial functions). No memoization. ---------------------'
    print "fibonacci(20)", timeit.timeit('fibonacci(20)', setup='from __main__ import fibonacci', number=1)
    print "factorial(5)", timeit.timeit('factorial(5)', setup='from __main__ import factorial', number=1)


    # Using memoization function "memoize" which does not support arguments
    print '---------------- First calculation timings with 1st set arguments: With Memoization ---------------------'
    print "memoize_fib(20)", timeit.timeit('memoize_fib(20)', setup='from __main__ import memoize_fib', number=1)
    print "memoize_fact(5)", timeit.timeit('memoize_fact(5)', setup='from __main__ import memoize_fact', number=1)


    # Below two statements should show almost same time as above.
    # 1st Set Repeat
    print '----------------------Repeat with 1st Set arguments : With Memoization -----------------------------'
    print "memoize_fib(20)", timeit.timeit('memoize_fib(20)', setup='from __main__ import memoize_fib', number=1)
    print "memoize_fact(5)", timeit.timeit('memoize_fact(5)', setup='from __main__ import memoize_fact', number=1)


    # 2nd Set
    print '-----------------First calculation timings with 2nd Set: With Memoization -----------------------'
    print "memoize_fib(5)", timeit.timeit('memoize_fib(5)', setup='from __main__ import memoize_fib', number=1)
    print "memoize_fact(8)", timeit.timeit('memoize_fact(8)', setup='from __main__ import memoize_fact', number=1)

    # This set calculation must begin to show improvement
    # 1st Set repeat
    print '-------------------Timings : Recalculating 1st set . Again. --------------------------'
    print "memoize_fib(20)", timeit.timeit('memoize_fib(20)', setup='from __main__ import memoize_fib', number=1)
    print "memoize_fact(5)", timeit.timeit('memoize_fact(5)', setup='from __main__ import memoize_fact', number=1)

    # This set calculation must begin to show improvement
    # 2nd Set repeat
    print '-------------------~Timings : Recalculating 2nd set--------------------------'
    print "memoize_fib(20)", timeit.timeit('memoize_fib(5)', setup='from __main__ import memoize_fib', number=1)
    print "memoize_fact(8)", timeit.timeit('memoize_fact(8)', setup='from __main__ import memoize_fact', number=1)

    # Let's see the cached values
    print '\nFactorial Cache', memoize_fact.__closure__[0].cell_contents

    print '\nFibo Cache', memoize_fib.__closure__[0].cell_contents
    
    print '\n-------------- Add Function memoized: With memoization (memoize_with_args) ------'
    print "Cache for add function before calling it.:",add.__closure__[0].cell_contents

    print 'Memoize with multiple arguments example'
    # 1st set first call with memoize
    print "Add : 2 + 3", add(2,3)
    print "Add 1,2,3,4,5", add(1,2,3,4,5)
    print "Cache after 1st call:", add.__closure__[0].cell_contents

    # 1st set,  second call with memoize
    print "Add : 2 + 3 :", add(2,3)
    print "Add 1,2,3,4,5 : ", add(1,2,3,4,5)
    print "Cache after 2nd call:", add.__closure__[0].cell_contents

    print '\n-------------- Multiply Function memoized with timer check : With memoization (my_memoize_with_args_and_timer) ------'
    print " Showing cache behaviour with same arguments used multiple times"
    
    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    print multiply(2,3,5)

    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    print multiply(2,3,5)

    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    print multiply(2,3,5)

    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    print multiply(2,3,5)

    print "Cache for multiply:", multiply.__closure__[0].cell_contents
    time.sleep(2) # This is to expire timer.
    print multiply(2,3,5)

    # Should see new expiry time
    print "Cache for multiply:", multiply.__closure__[0].cell_contents

    

    print '\n -------------- Testing performance of Class based Memoization technique on "sum_of_square" function ------'
    # Note: The decorator has been set to expire cache in 2 second
    print '1st set call...Expected max time'
    print '1st call time:', timeit.timeit('sum_of_square(2,3,4)', 'from __main__ import sum_of_square', number=1)
    print '2nd Call time:', timeit.timeit('sum_of_square(2,3,4)', 'from __main__ import sum_of_square', number=1)
    print '3rd Call time:', timeit.timeit('sum_of_square(2,3,4)', 'from __main__ import sum_of_square', number=1)
    time.sleep(2)
    print '4th Call. Timer should have expired by now:', timeit.timeit('sum_of_square(2,3,4)', 'from __main__ import sum_of_square', number=1)




