import datetime as dt
import time


def timer_expired(expiry_time):
    """
    This function tests if timer has expired
    I/P : datetime object
    O/P: bool
    """
    if dt.datetime.today() > expiry_time:
        return True
    else:
        return False

def calculate_expiry_time(timeout):
    """
    This function calculates expiry time .
    I/O: timeout in seconds
    O/P: datetime object
    """
    exp_time = dt.datetime.today() + dt.timedelta(seconds=timeout)
    return exp_time


def memoize(f):
    """
    Function: memoize
    I/P: function
    O/P: resolver function
    """
    cache = dict()
    def resolver(var):
        if var not in cache:
            cache[var] = f(var)
        return cache[var]
    return resolver

def memoize_with_args(f):
    """
        Function: memoize_with_args
        I/P: function
        Resolver Input: *args
        O/P: resolver function
    """
    cache = dict()
    def resolver(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return resolver

def memoize_with_args_and_timer(f, expire_in=None):
    """
        Function: memoize_with_args
        I/P: function
        Resolver Input: *args
        O/P: resolver function
    """
    cache = dict()

    def resolver(*args):
        if args in cache:

            if expire_in:
            	if 'expiry_{}'.format(args) not in cache:
                    print 'Expiry time not in cache'
                    expiry_time = calculate_expiry_time(expire_in)
                    cache['expiry_{}'.format(args)] = expiry_time
            	else:
                    print 'Expiry in cache'

                    #Get expiry time from cache
                    expiry_time = cache['expiry_{}'.format(args)]

                    # Check if timer expired.
                    if timer_expired(expiry_time):
                        print 'Timer expired'
                        new_expiry_time = calculate_expiry_time(expire_in)
                        cache['expiry_{}'.format(args)] = new_expiry_time
                    else:
                        print 'Timer Not expired yet'
                        return cache[args]
        cache[args] = f(*args)
        return cache[args]
    return resolver


