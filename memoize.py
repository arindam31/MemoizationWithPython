import datetime as dt
import time

"""
Function: memoize
I/P: function, args, timeout
O/P: result of calculation
"""
memoize_dict = {}


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
    cache = dict()
    def resolver(var):
        if var not in cache:
            cache[var] = f(var)
        return cache[var]
    return resolver
