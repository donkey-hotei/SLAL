import unittest
from SLAL.vector import Vector

class TestVectorClass(unittest.TestCase):
    """
    Test suite the vector class.
    """
    def test_setitem_and_getitem(self):
        """Test __setitem__ and __getitem__ """
        domain = range(0, 3)
        v = Vector(domain)
        v[0] = 42
        self.assertEqual(v[0], 42)

    def test_shallow_copy(self):
        """ Test copy method. """
        v = Vector()
        w = v.copy()
        self.assertFalse(v is w)

    def test_sparsity_convention(self):
        """Test __getitem__ with element doesn't exist."""
        domain = range(1, 4)
        v = Vector(domain)
        # check the sparisty convention with no elements set
        self.assertEqual(v[0], 0)
        # a vector without a domain is always zero
        v = Vector()
        self.assertEqual(v[0], 0)
        self.assertEqual(v[42], 0)

    def test_vector_negation(self):
        """Test __neg__ method. """
        domain = range(10)
        function = dict(zip(domain, range(1, 11)))
        v = Vector(domain, function)
        v = -v
        self.assertTrue(all(i < 0 for i in v))

    def test_vector_equality(self):
        """ Test __eq__ method. """
        domain = function = range(1, 4)
        v = Vector(domain, function)
        w = Vector(domain, function)
        self.assertTrue(v == w)

    def test_dot_product(self):
        """ Test __mul__ method with vector. """
        domain = function = range(1, 4)
        v = Vector(domain, function)
        w = Vector(domain, function)
        # sum [ 1 * 1 , 2 * 2, 3 * 3 ]
        self.assertEqual(v * w, 14)

    def test_vector_scalar_mult(self):
        """ Test __mul__ method with scalar. """
        c = 42
        domain = function = range(1, 4)
        v = Vector(domain, function)
        w = Vector(v.D, [42, 84, 126])
        self.assertEqual(c * v, w)

    def test_vector_addition(self):
        """ Test __add__ method. """
        domain = function = range(1, 4)
        v = Vector(domain, function)
        w = Vector(domain, function)
        res = Vector(domain, [2, 4, 6])
        self.assertEqual(v + w, res)

    def test_vector_subtraction(self):
        """ Test __sub__ method. """
        domain = function = range(1, 4)
        v = Vector(domain, function)
        w = Vector(domain, function)
        res = Vector(domain, [0, 0, 0])
        self.assertEqual(v - w, res)

    def test_vector_exponentation(self):
        """ Test __pow__ method. """
        domain = function = range(1, 4)
        v = Vector(domain, function)
        res_one = Vector(domain, [1, 4, 9])
        res_two = Vector(domain, [1, 16, 81])
        self.assertEqual(v**1, v)
        self.assertEqual(v**2, res_one)
        self.assertEqual(v**3, res_two)

    def test_scalar_division(self):
        """ Test __truediv__ method. """
        c = 2.
        domain = function =  range(1, 4)
        v = Vector(domain, function)
        res = Vector(domain, [0.5, 1.0, 1.5])
        self.assertEqual(v / c, res)

    def test_sum_list_of_vectors(self):
        """ Test __radd__ method. """
        domain = range(1, 11)
        vector_list = []
        for _ in range(10):
            v = Vector(domain, [1 for _ in domain])
            vector_list += [v]

        res = Vector(domain, [10 for _ in domain])
        self.assertEqual(sum(vector_list), res)

    def test_vector_eucldiean_length(self):
        """ Test length method. """
        domain = function = range(1, 4)
        v = Vector(domain, function)



if __name__ == '__main__':
    unittest.main()

