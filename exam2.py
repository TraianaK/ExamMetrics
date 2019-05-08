import unittest
import math


def square_numbers(a):
    if type(a) != type(1):
        return False
    return math.sqrt(a)


class TestParamaters(unittest.TestCase):
    "testing parameters"
    # tdd

    def test_correct_param(self):
        print("stignah")
        self.assertEqual(3, square_numbers(9))

    def test_false_param(self):
        self.assertEqual(square_numbers("pesho"), False)

    def test_missing_param(self):
        with self.assertRaises(TypeError):
            square_numbers()


if __name__ == "__main__":
    unittest.main(
    # defaultTest = "TestParamaters.test_sqrt"
    )
