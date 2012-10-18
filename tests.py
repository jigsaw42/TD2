from addition import *
import unittest

class test_addition(unittest.TestCase):
	
	def test_add(self):
		self.assertEqual(addition(2,3), 5)


