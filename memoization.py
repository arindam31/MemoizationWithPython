import datetime as dt


"""
Function: memoize
I/P: function, args, timeout
"""
memoize_dict = {}


def timer_expired(timeout, expiry_time=None):
	if not expiry_time:
		expiry_time = dt.datetime.today() + dt.timedelta(seconds=timeout)
		return True
	if dt.datetime.today() > expiry_time:
		expiry_time = None
		return True
	else:
		return False

def memoize(func, *args):
	if func.__name__ in memoize_dict.keys():
		return memoize_dict[func.__name__]['result'], 'Memoized'
	else:
		result = func(*args)
		memoize_dict[func.__name__] = {'arg': args, 'result': result}
		#timer_expired(timeout=5000)
		return result, 'First Calculation'



if __name__ == '__main__':
	def fun1(x,y):return x + y;
	def fun2(x,y):return x * y;
	result = memoize(fun1, 10, 20)
	result1 = memoize(fun1, 10, 20)
	result2 = memoize(fun2, 10, 20)
	print result, result1, result2




