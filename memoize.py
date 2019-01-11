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
