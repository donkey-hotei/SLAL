"""
 ___  __      __    __
/ __)(  )    /__\  (  )
\__ \ )(__  /(__)\  )(__
(___/(____)(__)(__)(____)
Sparse Linear Algebra Library
"""
import math


class Vector:

    """
    A vector has two fields:
    D - the domain (a set)
    f - a dictionary mapping (some) domain elements to field elements
        elements of D not appearing in f are implicitly mapped to zero
    """

    def __init__(self, labels=set(), function={}):
        self.D = labels
        self.f = function  # maps from domain to image

    # the __getitem__ function hangs when called by __mul__ ...
    def __getitem__(self, d):
        """ Return the value of entry d in v. """
        return self.f[d] if d in self.f else 0

    def __setitem__(self, k, val):
        """ Setting the element v with label d to be val """
        if k not in self.D:
            return None
        else:
            self.f[k] = val

    def __neg__(self):
        """ Negates the values of the vector. """
        return Vector(self.D, {label: -self[label] for label in self.f.keys()})

    # Multiply a vector by a scalar number
    def __rmul__(self, alpha):
        """ Scale a vector. """
        return Vector(self.D, {label: alpha * self[label]
                               for label in self.f.keys()})

    # __rmul__ = scalar_mul #if left arg of * is primitive, assume it's a
    # scalar

    def __mul__(self, other):
        """ Take dot product of two vectors. """
        # If other is a vector, returns the dot product of self and other
        if isinstance(other, Vector):
            assert self.D == other.D
            return sum([self[i] * other[i] for i in self.D])
        else:
            # Will cause other.__rmul__(self) to be invoked
            return NotImplemented

    def __truediv__(self, other):  # Scalar division
        return (1 / other) * self

    def __add__(self, other):
        # assert self.D == other.D
        if isinstance(other, int):
            raise Exception("Cannot add number with vector.")
        return Vector(self.D, {i: self[i] + other[i] for i in self.D})

    def __radd__(self, other):
        "Simple hack to allow sum(...) to work with vectors"
        if other == 0:  # Otherwise sum(...) would return a value of type int
            return self

    def __sub__(a, b):
        "Returns a vector which is the difference of a and b."
        return a + (-b)

    def __eq__(self, other):
        assert self.D == other.D
        # this is clearly a recursive cal
        return [self[e] for e in self.D] == [other[e] for e in other.D]

    def __pow__(self, exponent):
        result = self
        for _ in range(exponent):
            result *= result
        return result

    def __str__(v):
        "pretty-printing"
        D_list = sorted(v.D, key=repr)  # sort the domain into a list
        numdec = 3  # max width used up for each number
        # wd is a dictionary that maps each element in the domain to a max
        # width
        wd = dict([(k, (1 + max(len(str(k)),
                                len('{0:.{1}G}'.format(v[k], numdec)))))
                   if isinstance(v[k], int)
                   or isinstance(v[k], float)
                   else (k, (1 + max(len(str(k)), len(str(v[k])))))
                   for k in D_list])
        # w = 1+max([len(str(k)) for k in D_list]+[len('{0:.{1}G}'.format(value,numdec)) for value in v.f.values()])
        s1 = ''.join(['{0:>{1}}'.format(k, wd[k]) for k in D_list])
        s2 = ''.join(['{0:>{1}.{2}G}'.format(v[k], wd[k], numdec)
                      if isinstance(v[k], int)
                      or isinstance(v[k], float)
                      else '{0:>{1}}'.format(v[k], wd[k])
                      for k in D_list])
        return "\n" + s1 + "\n" + '-' * sum(wd.values()) + "\n" + s2

    def __repr__(self):
        return "Vector(" + str(self.D) + "," + str(self.f) + ")"

    def copy(self):
        """" Don't make a new copy of the domain D """
        return Vector(self.D, self.f.copy())

    def __len__(self):
        """ return number of elements in the vector
        """
        return len(self.f.iteritems())

    def length(self):
        """  Euclidean length of vector """
        return math.sqrt(sum(Vector(self.D, {i: self[i] * self[i]
                                             for i in self.D})))
