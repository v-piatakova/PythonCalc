from calculation.calculation_module import calculation
import unittest


class NameTestCase(unittest.TestCase):
    def test_calculation(self):
        result = calculation ('(35+5)*6/8+3')
        print(result)
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()