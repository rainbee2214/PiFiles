from ..Pi import pi
import unittest

class TestAccuracy(unittest.TestCase):
    """Tests the accuracy of hex digits of pi"""

    def setup(self):
        pass

    def test_01_Ones(self):
        self.assertFalse(pi.verifyIndex(-1))
        self.assertTrue(pi.verifyIndex(0))
        self.assertTrue(pi.verifyIndex(2))
        self.assertTrue(pi.verifyIndex(8))

    def test_02_Tens(self):
        self.assertTrue(pi.verifyIndex(10))
        self.assertTrue(pi.verifyIndex(50))

    def test_03_Hundreds(self):
        self.assertTrue(pi.verifyIndex(100))
        self.assertTrue(pi.verifyIndex(500))

    def test_04_Thousands(self):
        self.assertTrue(pi.verifyIndex(1000))
        self.assertTrue(pi.verifyIndex(5000))

    def test_05_TenThousands(self):
        self.assertTrue(pi.verifyIndex(10000))
        self.assertTrue(pi.verifyIndex(50000))

    def test_06_HundredThousands(self):
        self.assertTrue(pi.verifyIndex(100000))
        self.assertTrue(pi.verifyIndex(500000))

    def test_07_Millions(self):
        self.assertTrue(pi.verifyIndex(1000000))
        self.assertTrue(pi.verifyIndex(5000000))

    def test_08_TenMillions(self):
        self.assertTrue(pi.verifyIndex(10000000))
        self.assertTrue(pi.verifyIndex(11000000))
        self.assertTrue(pi.verifyIndex(11500000))
        self.assertTrue(pi.verifyIndex(11800000))
        self.assertTrue(pi.verifyIndex(11900000))
        self.assertTrue(pi.verifyIndex(12000000))
        self.assertTrue(pi.verifyIndex(12500000))
        self.assertTrue(pi.verifyIndex(13000000))
        
if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)
