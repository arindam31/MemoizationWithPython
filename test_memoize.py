import unittest
import memoize
import time
import datetime
from myfunctions import *

class TestMemoize(unittest.TestCase):

	
	def setUp(self):
		self.memoize_fib = memoize.memoize(fibonacci)
		self.memoize_fact = memoize.memoize(factorial)

	def tearDown(self):
		del self.memoize_fib
		del self.memoize_fact

	def test_resolver(self):
		cache = self.memoize_fib.__closure__[0].cell_contents
		self.assertFalse(cache, 'Cache not empty:%s' % cache)
		self.memoize_fib(5)
		self.assertTrue(5 in self.memoize_fib.__closure__[0].cell_contents)



		