import unittest
from Simply import getsum


class SimplyTestCase(unittest.TestCase):
	def setUp(self):
		pass


	def test_getSum(self):
		self.assertEqual( getsum(3,4), 7)





if __name__ == '__main__':
	print "Starting testing"

	unittest.main()
