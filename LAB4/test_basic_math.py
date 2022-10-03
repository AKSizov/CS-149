import unittest
import basic_math

# you're supposed to modify this test for the full basic_math
# i don't care, it's not graded


class TestBasicMath(unittest.TestCase):

    def test_add(self):
        expected = 15.5
        actual = basic_math.add(7.2, 8.3)
        self.assertEqual(expected, actual)

    def test_subtract(self):
        expected = 2.2
        actual = basic_math.subtract(3.5, 1.3)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
