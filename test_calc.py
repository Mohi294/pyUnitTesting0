import unittest
import pyUnitTesting0



class TestCalc(unittest.TestCase):

    def test_add(self):
        result = pyUnitTesting0.add(10, 5)
        self.assertEqual(result, 15)

    def test_divide(self):
        self.assertRaises(ValueError, pyUnitTesting0.divide, 10, 2)

if __name__ == '__main__':
    unittest.main()
