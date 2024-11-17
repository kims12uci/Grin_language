from grin.base_object_class import *
import unittest

class TestBaseClass(unittest.TestCase):
    def test_eq_true(self):
        o1 = grinObject(1)
        o2 = grinObject(1)
        self.assertEqual(o1, o2)

    def test_eq_false(self):
        o1 = grinObject(1)
        o2 = grinObject(2)
        self.assertNotEqual(o1, o2)

    def test_eq_false_not_grinObj(self):
        o1 = grinObject(1)
        o2 = 1
        self.assertNotEqual(o1, o2)

    def test_hash_equal_grinObj(self):
        o1 = grinObject(1)
        o2 = grinObject(1)
        self.assertEqual(hash(o1), hash(o2))

    def test_lt_true(self):
        o1 = grinObject(1)
        o2 = grinObject(2)
        self.assertEqual(o1 < o2, True)

    def test_lt_false_grinObjects(self):
        o1 = grinObject(1)
        o2 = grinObject(1)
        self.assertEqual(o1 < o2, False)

    def test_lt_not_grinObject(self):
        o1 = grinObject(1)
        with self.assertRaises(runtimeError):
            a = o1 < 1

    def test_le_true_less(self):
        o1 = grinObject(1)
        o2 = grinObject(2)
        self.assertEqual(o1 <= o2, True)

    def test_le_true_equal(self):
        o1 = grinObject(1)
        o2 = grinObject(1)
        self.assertEqual(o1 <= o2, True)

    def test_le_false(self):
        o1 = grinObject(2)
        o2 = grinObject(1)
        self.assertEqual(o1 <= o2, False)

    def test_le_not_grinObject(self):
        o1 = grinObject(1)
        with self.assertRaises(runtimeError):
            a = o1 <= 1

    def test_repr(self):
        o1 = grinObject(1)
        self.assertEqual(o1.__repr__(), 1)

if __name__ == '__main__':
    unittest.main()