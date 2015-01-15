"""
SLAL: Vector Utility Functions
by dysnsne
(c)opyleft
"""
from vector import Vector

# utility functions for vectors 
def list2vector(L):
    """Turn a list of length n into a n-vector"""
    return Vector(set(range(len(L))), { k : v for (k, v) in enumerate(L)})

def vector2list(V):
    """ Turn vector into list. """
    return [ V[e] for e in V.D ]
    
def zero_vector(n):
    """ Builds a zero vector of length-n. """
    return Vector(set(range(n)), {} )

def linear_comb(vlist, clist):
    """ Returns the vector that is the linear combination
    of all the vectors in vlist with corresponding coeffs in clist. """
    return sum([coeff * v for (coeff,v) in zip(clist, vlist)])    

# Vectors in containers
def vector_select(veclist, k):
    """ Return a list of all the vectors in vectorlist whose k-value is zero."""
    return [ v for v in vectorlist if v[k] == 0 ]

def vector_sum(veclist): 
    """ Sums a list of vectors. """
    return sum(veclist, Vec(veclist[0].D, {} ))

def vector_select_sum(veclist, k):
    return vector_sum(vector_select(veclist, k))

def scale_vectors(vecdict):
    """ Take a dictionary mapping positive numbers to
        instances of the Vector class and outputs a list
        of scaled vectors by a fraction of their corresponding key.
    """
    return [ (1/k) * v for v,k in vecdict.iteritems() ]

def triangular_solve(rowlist, b, label_list):
    """
    Input: for some positive integer n, a list rowlist of
           vectors all having the same n-element domain D,
           a list label_list consisting of the elements of D,
           and a list b of n-numbers.
    Output: the vector x such that for i in [1, .., n-1], the
            dotproduct of the rowlist[i] and x equals b...
    """
    D = rowlist[0].D
    x = zero_vector(len(D))
    
    for j in reversed(range(len(D))):
        c = label_list[j]
        row = rowlist[j]
        x[c] = (b[j] - x*row)/row[c]
    return x
