import datetime as dt
import time


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
	

def memoize(func, *args, **kwargs):
	"""
	Function: memoize
	I/P: function, args, timeout
	O/P: result of calculation
	"""

	#If timeout is provided, get that, or else, use default.
	timeout = kwargs.pop('timeout', 5000)
	
	if func.__name__ in memoize_dict.keys():
		if set(args) == set(memoize_dict[func.__name__]['arg']):
			if not timer_expired(memoize_dict[func.__name__]['expiry_time']):
				return memoize_dict[func.__name__]['result'], 'Memoized'
			
	result = func(*args)
	memoize_dict[func.__name__] = {'arg': args, 'result': result, 'expiry_time': calculate_expiry_time(timeout)}
	
	return result, 'First Calculation'



if __name__ == '__main__':
	def fun1(x,y):return x + y;
	def fun2(x,y):return x * y;
	result = memoize(fun1, 10, 20, timeout=2)
	time.sleep(1)
	result1 = memoize(fun1, 10, 20)
	time.sleep(3)
	result2 = memoize(fun1, 10, 20)
	result3 = memoize(fun1, 99, 1)
	print result, result1, result2, result3




