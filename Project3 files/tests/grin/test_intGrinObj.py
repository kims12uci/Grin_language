from grin.int_grin_object import intGrinObj
from grin.str_grin_object import strGrinObj
from grin.float_grin_object import floatGrinObj
from grin.base_object_class import runtimeError
import unittest

class testIntGrinObj(unittest.TestCase):
    def test_add_two_intGrin(self):
        i1 = intGrinObj(1)
        i2 = intGrinObj(2)
        i3 = intGrinObj(3)
        self.assertEqual(i1 + i2, i3)

    def test_add_floatGrin(self):
        i1 = intGrinObj(1)
        f1 = floatGrinObj(3.5)
        f2 = floatGrinObj(4.5)
        self.assertEqual(i1 + f1, f2)

    def test_add_neg_intGrin(self):
        i1 = intGrinObj(1)
        i2 = intGrinObj(-2)
        i3 = intGrinObj(-1)
        self.assertEqual(i1 + i2, i3)

    def test_add_invalid_adder(self):
        i1 = intGrinObj(1)
        with self.assertRaises(runtimeError):
            a = i1 + 1

    def test_sub_two_intGrin(self):
        i1 = intGrinObj(4)
        i2 = intGrinObj(1)
        i3 = intGrinObj(3)
        self.assertEqual(i1 - i2, i3)

    def test_sub_floatGrin(self):
        i1 = intGrinObj(4)
        f1 = floatGrinObj(3.5)
        f2 = floatGrinObj(0.5)
        self.assertEqual(i1 - f1, f2)

    def test_sub_invalid(self):
        i1 = intGrinObj(1)
        with self.assertRaises(runtimeError):
            a = i1 - 1

    def test_mul_two_intGrin(self):
        i1 = intGrinObj(2)
        i2 = intGrinObj(3)
        i3 = intGrinObj(6)
        self.assertEqual(i1 * i2, i3)

    def test_mul_floatGrin(self):
        i1 = intGrinObj(4)
        f1 = floatGrinObj(0.5)
        f2 = floatGrinObj(2.0)
        self.assertEqual(i1 * f1, f2)

    def test_mul_strGrin(self):
        i1 = intGrinObj(2)
        s1 = strGrinObj("'hi'")
        s2 = strGrinObj('hihi')
        self.assertEqual(i1 * s1, s2)

    def test_mul_invalid(self):
        i1 = intGrinObj(1)
        with self.assertRaises(runtimeError):
            a = i1 * 1

    def test_div_two_intGrin(self):
        i1 = intGrinObj(7)
        i2 = intGrinObj(3)
        i3 = intGrinObj(2)
        self.assertEqual(i1 / i2, i3)

    def test_div_floatGrin(self):
        i1 = intGrinObj(7)
        f1 = floatGrinObj(2.0)
        f2 = floatGrinObj(3.5)
        self.assertEqual(i1 / f1, f2)

    def test_div_invalid_0_intGrin(self):
        i1 = intGrinObj(1)
        i2 = intGrinObj(0)
        with self.assertRaises(runtimeError):
            a = i1 / i2

    def test_div_invalid_0_floatGrin(self):
        i1 = intGrinObj(1)
        i2 = floatGrinObj(0)
        with self.assertRaises(runtimeError):
            a = i1 / i2

    def test_div_invalid_type(self):
        i1 = intGrinObj(1)
        with self.assertRaises(runtimeError):
            a = i1 / 2

    def test_lt_two_int_true(self):
        i1 = intGrinObj(1)
        i2 = intGrinObj(3)
        self.assertTrue(i1 < i2)

    def test_lt_two_int_false(self):
        i1 = intGrinObj(1)
        i2 = intGrinObj(1)
        self.assertFalse(i1 < i2)

    def test_lt_float_true(self):
        i1 = intGrinObj(1)
        f1 = floatGrinObj(3.0)
        self.assertTrue(i1 < f1)

    def test_lt_float_false(self):
        i1 = intGrinObj(1)
        f1 = floatGrinObj(1.0)
        self.assertFalse(i1 < f1)

    def test_lt_invalid(self):
        i1 = intGrinObj(1)
        with self.assertRaises(runtimeError):
            a = i1 < 3

    def test_le_two_int_true(self):
        i1 = intGrinObj(1)
        i2 = intGrinObj(3)
        self.assertTrue(i1 <= i2)

    def test_le_two_int_false(self):
        i1 = intGrinObj(2)
        i2 = intGrinObj(1)
        self.assertFalse(i1 <= i2)

    def test_le_float_true(self):
        i1 = intGrinObj(1)
        f1 = floatGrinObj(3.0)
        self.assertTrue(i1 <= f1)

    def test_le_float_false(self):
        i1 = intGrinObj(2)
        f1 = floatGrinObj(1.0)
        self.assertFalse(i1 <= f1)

    def test_le_invalid(self):
        i1 = intGrinObj(1)
        with self.assertRaises(runtimeError):
            a = i1 <= 3

if __name__ == '__main__':
    unittest.main()