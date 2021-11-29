from parse_function import parse
import unittest


class NameTestCase(unittest.TestCase):
    def test_entered_string(self):
        result = parse('(35+5)*6/8+3')
        print(result)
        self.assertEqual(result, ['(', '35', '+', '5', ')', '*', '6', '/', '8', '+', '3'])


if __name__ == "__main__":
    unittest.main()
