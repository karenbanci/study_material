import unittest
import currency_converter as cc


class TestCC(unittest.TestCase):

    def test_bad_currencies(self):
        with self.assertRaises(KeyError):
            cc.currency_converter(10, "AQW", "NZD")
        with self.assertRaises(KeyError):
            cc.currency_converter(10, "NZD", "AQW")

    def test_non_positive_qty(self):
        with self.assertRaises(ValueError):
            cc.currency_converter(-1, "NZD", "USD")

    def test_return_values(self):
        self.assertEqual(8, cc.currency_converter(10, "USD", "GBP"))
        self.assertAlmostEqual(0.71, cc.currency_converter(1, "CAD", "USD"), 2)
        self.assertEqual(2.8, cc.currency_converter(1.8, "EUR", "CAD"))


if __name__ == "__main__":
    unittest.main()
