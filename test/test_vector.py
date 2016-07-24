import unittest
from SLAL.vector import Vector

class TestVectorClass(unittest.TestCase):
    """
    Test suite the vector class.
    """
    def test_setitem_and_getitem(self):
        """Test __setitem__ and __getitem__ """
        v = Vector(labels={i for i in range(10)})
        v[0] = 42
        self.assertEqual(v[0], 42)

    def test_sparsity_convention(self):
        """Test __getitem__ with element doesn't exist."""
        v = Vector(labels={i for i in range(10)})
        # check the sparisty convention with no elements set
        self.assertEqual(v[0], 0)
        # a vector without a domain is always zero
        v = Vector()
        self.assertEqual(v[0], 0)
        self.assertEqual(v[42], 0)

    def test_vector_negation(self):
        """Test __neg__ method. """
        # a vector defined as f: [0..9] -> [1..10]
        v = Vector(range(10), dict(zip(range(10), range(1, 11))))
        v = -v
        self.assertTrue(all(i < 0 for i in v))

    def test_vector_equality(self):
        """ Test __eq__ method. """
        v = Vector(range(1, 4), range(1, 4))
        w = Vector(range(1, 4), range(1, 4))
        self.assertTrue(v == w)

    def test_dot_product(self):
        """ Test __mul__ method with vector. """
        domain = range(1, 4)
        v = Vector(domain, dict(zip(domain, domain)))
        w = Vector(domain, dict(zip(domain, domain)))
        # sum [ 1 * 1 , 2 * 2, 3 * 3 ]
        self.assertEqual(v * w, 14)

    def test_vector_scalar_mult(self):
        """ Test __mul__ method with scalar. """
        c = 42
        domain = range(1, 4)
        v = Vector(domain, dict(zip(domain, domain)))
        w = Vector(v.D, [42, 84, 126])
        self.assertEqual(c * v, w)

    def test_vector_addition(self):
        """ Test __add__ method. """
        domain = range(1, 4)
        v = Vector(domain, dict(zip(domain, domain)))
        w = Vector(domain, dict(zip(domain, domain)))
        res = Vector(domain, [2, 4, 6])
        self.assertEqual(v + w, res)

    def test_vector_subtraction(self):
        """ Test __sub__ method. """
        pass

    def test_vector_exponentation(self):
        pass



if __name__ == '__main__':
    unittest.main()

