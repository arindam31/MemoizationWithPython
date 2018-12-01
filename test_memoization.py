import unittest
import memoization

class MemoizeTest(unittest.TestCase):
	def test_memoize_without_timeout(self):
		"""
			Test I/P: Function and arguments, no timeout
			O/P : Return value of function
		"""
		def add_func(a, b):
			return a + b
		from_memoize, message = memoization.memoize(add_func, 10, 20)
		self.assertEqual(from_memoize, 30)
		self.assertEqual(message, 'First Calculation')	

		from_memoize, message = memoization.memoize(add_func, 10, 20)
		self.assertEqual(from_memoize, 30)
		self.assertEqual(message, 'Memoized')

if __name__ == '__main__':
	unittest.main()
		
