from OPZ.OPZ_module import OPZ
import unittest


class OPZTestCase(unittest.TestCase):
    def test_parsed_string(self):
        result = OPZ("(3+4)*2+7-8-2")
        print(result)
        self.assertEqual(result, ['3', '4', '+', '2', '*', '7', '+', '8', '-', '2', '-', ')'])


if __name__ == "__main__":
    unittest.main()
