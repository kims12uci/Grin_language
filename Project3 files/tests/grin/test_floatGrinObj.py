from grin.int_grin_object import intGrinObj
from grin.float_grin_object import floatGrinObj
from grin.base_object_class import runtimeError
import unittest

class testFloatGrinObj(unittest.TestCase):
    def test_add_two_floatGrin(self):
        f1 = floatGrinObj(1)
        f2 = floatGrinObj(2)
        f3 = floatGrinObj(3)
        self.assertEqual(f1 + f2, f3)

    def test_add_intGrin(self):
        i1 = intGrinObj(1)
        f1 = floatGrinObj(3.5)
        f2 = floatGrinObj(4.5)
        self.assertEqual(f1 + i1, f2)

    def test_add_invalid_adder(self):
        f1 = floatGrinObj(1)
        with self.assertRaises(runtimeError):
            a = f1 + 1

    def test_sub_two_floatGrin(self):
        f1 = floatGrinObj(4)
        f2 = floatGrinObj(1)
        f3 = floatGrinObj(3)
        self.assertEqual(f1 - f2, f3)

    def test_sub_intGrin(self):
        i1 = intGrinObj(2)
        f1 = floatGrinObj(3.5)
        f2 = floatGrinObj(1.5)
        self.assertEqual(f1 - i1, f2)

    def test_sub_invalid(self):
        f1 = floatGrinObj(1)
        with self.assertRaises(runtimeError):
            a = f1 - 1.5

    def test_mul_two_floatGrin(self):
        f1 = floatGrinObj(2.5)
        f2 = floatGrinObj(4)
        f3 = floatGrinObj(10)
        self.assertEqual(f1 * f2, f3)

    def test_mul_intGrin(self):
        i1 = intGrinObj(4)
        f1 = floatGrinObj(0.5)
        f2 = floatGrinObj(2.0)
        self.assertEqual(f1 * i1, f2)

    def test_mul_invalid(self):
        f1 = floatGrinObj(1)
        with self.assertRaises(runtimeError):
            a = f1 * 1

    def test_div_two_floatGrin(self):
        f1 = floatGrinObj(7.2)
        f2 = floatGrinObj(3.6)
        f3 = floatGrinObj(2.0)
        self.assertEqual(f1 / f2, f3)

    def test_div_intGrin(self):
        i1 = intGrinObj(3)
        f1 = floatGrinObj(3.6)
        f2 = floatGrinObj(1.2)
        self.assertEqual(f1 / i1, f2)

    def test_div_invalid_0_intGrin(self):
        f1 = floatGrinObj(1)
        i1 = intGrinObj(0)
        with self.assertRaises(runtimeError):
            a = f1 / i1

    def test_div_invalid_0_floatGrin(self):
        f1 = floatGrinObj(1)
        f2 = floatGrinObj(0)
        with self.assertRaises(runtimeError):
            a = f1 / f2

    def test_div_invalid_type(self):
        f1 = floatGrinObj(1)
        with self.assertRaises(runtimeError):
            a = f1 / 2

    def test_lt_two_float_true(self):
        f1 = floatGrinObj(1.5)
        f2 = floatGrinObj(3.7)
        self.assertTrue(f1 < f2)

    def test_lt_two_float_false(self):
        f1 = floatGrinObj(4.5)
        f2 = floatGrinObj(3.7)
        self.assertFalse(f1 < f2)

    def test_lt_int_true(self):
        i1 = intGrinObj(7)
        f1 = floatGrinObj(3.2)
        self.assertTrue(f1 < i1)

    def test_lt_int_false(self):
        i1 = intGrinObj(1)
        f1 = floatGrinObj(1.0)
        self.assertFalse(f1 < i1)

    def test_lt_invalid(self):
        f1 = floatGrinObj(1.3)
        with self.assertRaises(runtimeError):
            a = f1 < 3

    def test_le_two_float_true(self):
        f1 = floatGrinObj(1.4)
        f2 = floatGrinObj(3.4)
        self.assertTrue(f1 <= f2)

    def test_le_two_float_false(self):
        f1 = floatGrinObj(2.7)
        f2 = floatGrinObj(1.3)
        self.assertFalse(f1 <= f2)

    def test_le_int_true(self):
        i1 = intGrinObj(6)
        f1 = floatGrinObj(3.1)
        self.assertTrue(f1 <= i1)

    def test_le_int_false(self):
        i1 = intGrinObj(1)
        f1 = floatGrinObj(4.5)
        self.assertFalse(f1 <= i1)

    def test_le_invalid(self):
        f1 = floatGrinObj(1.3)
        with self.assertRaises(runtimeError):
            a = f1 <= 3


if __name__ == '__main__':
    unittest.main()