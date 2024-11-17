from grin.base_object_class import runtimeError
from grin.int_grin_object import intGrinObj
from grin.str_grin_object import strGrinObj
import unittest

class testStrGrinObj(unittest.TestCase):
    def test_add_normal_case(self):
        s1 = strGrinObj("'hi'")
        s2 = strGrinObj("'hello'")
        s3 = strGrinObj('hihello')
        self.assertEqual(s1 + s2, s3)

    def test_add_normal_empty(self):
        s1 = strGrinObj("'hi'")
        s2 = strGrinObj('')
        s3 = strGrinObj('hi')
        self.assertEqual(s1 + s2, s3)

    def test_add_invalid(self):
        s1 = strGrinObj('hi')
        with self.assertRaises(runtimeError):
            s2 = s1 + 'hello'

    def test_mul_normal(self):
        s1 = strGrinObj("'hi'")
        i1 = intGrinObj(3)
        s2 = strGrinObj('hihihi')
        self.assertEqual(s1 * i1, s2)

    def test_mul_normal_0(self):
        s1 = strGrinObj('hi')
        i1 = intGrinObj(0)
        s2 = strGrinObj('')
        self.assertEqual(s1 * i1, s2)

    def test_mul_normal_empty(self):
        s1 = strGrinObj('')
        i1 = intGrinObj(3)
        self.assertEqual(s1 * i1, s1)

    def test_mul_invalid(self):
        s1 = strGrinObj('hi')
        with self.assertRaises(runtimeError):
            a = s1 * 4

if __name__ == '__main__':
    unittest.main()