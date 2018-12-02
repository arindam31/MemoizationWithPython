import unittest
import memoization

class MemoizeTest(unittest.TestCase):

	def setUp(self):
		memoization.memoize_dict = {}
		
	def add_func(self, a, b):
		return a + b

	def multiply_func(self, a, b):
		return a * b 

	def test_memoize_function_with_default_timeout_using_single_function_with_same_arguments(self):
		"""
		Tests Steps:
			1) Call memoize with function with arguments
			2) Assert results 
			3) Call memoize with function with same arguments
		"""
		
		from_memoize, message = memoization.memoize(self.add_func, 10, 20)
		self.assertEqual(from_memoize, 30)
		self.assertEqual(message, 'First Calculation', 
			'Expected this to be first calculation')	

		from_memoize, message = memoization.memoize(self.add_func, 10, 20)
		self.assertEqual(from_memoize, 30)
		self.assertEqual(message, 'Memoized', 'Expected this to come from memoized result bank')

	def test_multi_functions_with_default_timeout_and_same_arguments(self):
		"""
		Test Steps: 
		
			1) Call function (add_func). This should be calculated by this function
			2) Call function (add_func) with same arguments again. Result should come from memoized result bank.
			3) Call another function (multiply_func). Result should be calculated.
			4) Call First function withe same arguments again. Result should come from memoized result bank.
		"""
		
		from_memoize, message = memoization.memoize(self.add_func, 11, 22)
		self.assertEqual(from_memoize, 33)
		self.assertEqual(message, 'First Calculation', 
			'Expected this to be first calculation')
		from_memoize, message = memoization.memoize(self.add_func, 11, 22)
		self.assertEqual(from_memoize, 33)
		self.assertEqual(message, 'Memoized', 'Expected this to come from memoized result bank')

		from_memoize, message = memoization.memoize(self.multiply_func, 5, 4)
		self.assertEqual(from_memoize, 20)
		self.assertEqual(message, 'First Calculation', 
			'Expected this to be first calculation')

	def test_single_function_with_default_timeout_and_different_arguments(self):
		"""
		Test Steps:
			1) Call function (add_func) with values v1 and v2. This should be calculated
			2) Call function (add_func) with values v3 and v4. This should be calculated
			3) Call function (add_func) with values v1 and v2. This should be calculated
		"""
		from_memoize, message = memoization.memoize(self.add_func, 11, 22)
		self.assertEqual(from_memoize, 33)
		self.assertEqual(message, 'First Calculation', 
			'Expected this to be first calculation')
		from_memoize, message = memoization.memoize(self.add_func, 100, 200)
		self.assertEqual(from_memoize, 300)
		self.assertEqual(message, 'First Calculation', 'Expected this to be first calculation')


if __name__ == '__main__':
	unittest.main()
		
