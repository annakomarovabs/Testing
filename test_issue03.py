import unittest
from one_hot_encoder import fit_transform


class TestOHE(unittest.TestCase):
    def test_part(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = ('Moscow', [0, 0, 1])
        self.assertIn(expected, actual)

    def test_instance(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        self.assertIsInstance(actual[0], tuple)

    def test_ft(self):
        actual = fit_transform('Cheese')
        expected = [('Cheese', [1])]
        self.assertEqual(expected, actual)

    def test_len(self):
        words = ['Moscow', 'New York', 'Moscow', 'London']
        actual = len(fit_transform(words)[0][1])
        expected = len(set(words))
        self.assertEqual(actual, expected)

    def test_exception(self):
        with self.assertRaises(Exception):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
