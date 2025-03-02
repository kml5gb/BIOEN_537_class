import unittest
from program import add, divide

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_bad_add(self):
        self.assertNotEqual(add(1, 2), 2)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)

    def test_bad_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(4, 0)

if __name__ == '__main__':
    unittest.main()


'''Can return the data type or you can use a set of values that you know the answer to.
For plots - can return information associated with the plot or use a smoke test'''