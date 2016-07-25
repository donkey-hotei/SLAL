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

    def test_shallow_copy(self):
        """ Test copy method. """
        v = Vector()
        w = v.copy()
        self.assertFalse(v is w)

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
        domain = range(1, 4)
        v = Vector(domain, domain)
        w = Vector(domain, domain)
        self.assertTrue(v == w)

    def test_dot_product(self):
        """ Test __mul__ method with vector. """
        domain = range(1, 4)
        v = Vector(domain, domain)
        w = Vector(domain, domain)
        # sum [ 1 * 1 , 2 * 2, 3 * 3 ]
        self.assertEqual(v * w, 14)

    def test_vector_scalar_mult(self):
        """ Test __mul__ method with scalar. """
        c = 42
        domain = range(1, 4)
        v = Vector(domain, domain)
        w = Vector(v.D, [42, 84, 126])
        self.assertEqual(c * v, w)

    def test_vector_addition(self):
        """ Test __add__ method. """
        domain = range(1, 4)
        v = Vector(domain, domain)
        w = Vector(domain, domain)
        res = Vector(domain, [2, 4, 6])
        self.assertEqual(v + w, res)

    def test_vector_subtraction(self):
        """ Test __sub__ method. """
        domain = range(1, 4)
        v = Vector(domain, domain)
        w = Vector(domain, domain)
        res = Vector(domain, [0, 0, 0])
        self.assertEqual(v - w, res)

    def test_vector_exponentation(self):
        """ Test __pow__ method. """
        domain = range(1, 4)
        v = Vector(domain, domain)
        res_one = Vector(domain, [1, 4, 9])
        res_two = Vector(domain, [1, 16, 81])
        self.assertEqual(v**1, v)
        self.assertEqual(v**2, res_one)
        self.assertEqual(v**3, res_two)

    def test_scalar_division(self):
        """ Test __truediv__ method. """
        c = 2.
        domain = range(1, 4)
        v = Vector(domain, domain)
        res = Vector(domain, [0.5, 1.0, 1.5])
        self.assertEqual(v / c, res)

    def test_sum_list_of_vectors(self):
        """ Test __radd__ method. """
        vector_list = []
        for _ in range(10):
            v = Vector(range(1, 11), [1 for _ in range(1, 11)])
            vector_list += [v]

        res = Vector(range(1, 11), [10 for _ in range(1, 11)])
        self.assertEqual(sum(vector_list), res)


if __name__ == '__main__':
    unittest.main()

