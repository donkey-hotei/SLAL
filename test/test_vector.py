import unittest
from SLAL.core.vector import Vector

class TestVectorClass(unittest.TestCase):
    """
    Test suite the vector class.
    """
    def test_setitem_and_getitem():
        # a vector defined over the range [0, 9]
        v = Vector(labels={i for i in range(10})
        # check the sparisty convention with no elements set
        self.assertEqual(v[0], 0)
        # check that the same index now has a value
        v[0] = 42
        self.assertEqual(v[0], 42)


if __name__ == '__main__':
    unitttest.run()
