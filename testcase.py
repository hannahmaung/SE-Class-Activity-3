import unittest
import unittesting


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(unittesting.add(2,1), 3)
    def test2(self):
        self.assertEqual(unittesting.subtract(10,5),5)
    def test3(self):
        self.assertEqual(unittesting.multiply(2,3),6)
    def test4(self):
        self.assertEqual(unittesting.divide(10,2),5)


if __name__ == '__main__': 
    unittest.main(verbosity=2)