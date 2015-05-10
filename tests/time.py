from ..Pi import pi
import unittest

class TestTime(unittest.TestCase):
	"""Tests the time to completion of hex digits of pi"""

	def setup(self):
		pass

	def test_01_Low(self):
		print ""
		pi.timedHex(-1)
		pi.timedHex(0)
		pi.timedHex(1)
		pi.timedHex(10)
		pi.timedHex(100)
		pi.timedHex(500)

	def test_02_Thousands(self):
		print ""
		pi.timedHex(1000)
		pi.timedHex(10000)
		pi.timedHex(100000)

	def test_03_Millions(self):
		print ""
		pi.timedHex(1000000)
		pi.timedHex(10000000)
		pi.timedHex(100000000)
		
if __name__ == '__main__':
	unittest.main(verbosity=2, failfast=True)
