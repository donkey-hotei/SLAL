"""
Vector Utility Functions
"""
from core.vector import Vector


def list2vector(L):
    """
    Input: L -> a list containing field elements
    Output: a Vector of length len(L)
    """
    return Vector(set(range(len(L))), {k: v for (k, v) in enumerate(L)})


def vector2list(V):
    """
    Input: V -> a Vector
    Output: a list consisting of the elements in V.
    """
    return [V[e] for e in V.D]


def zero_vector(n):
    """
    Input: n -> an integer
    Output: an n-length vector consisting of zeros.
    """
    return Vector(set(range(n)), {})


def linear_comb(vlist, clist):
    """
    Input: vlist -> a list of Vectors, [v_1, ..., v_n]
           clist -> a list of coefficents, [c_1, ..., c_n]
    Output: result of a linear combination, c_1 * v_1 + ... + c_n * v_n
    """
    return sum([coeff * v for (coeff, v) in zip(clist, vlist)])


def vector_select(veclist, k):
    """ Return a list of all the vectors
        in vectorlist whose k-value is zero.
    """
    return [v for v in veclist if v[k] == 0]


def vector_sum(veclist):
    """
    Input: veclist -> a list of Vector
    Output: a sum of all the Vectors in veclist
    """
    # default value is an zero-vector
    return sum(veclist, Vector(veclist[0].D, {}))


def vector_select_sum(veclist, k):
    return vector_sum(vector_select(veclist, k))


def scale_vectors(vecdict):
    """
    Input: vecdict -> a dictionary mapping positive numbers
                    to Vectors
    Output: a list of scaled vectors by a fraction of their
            corresponding key.
    """
    return [(1 / k) * v for v, k in vecdict.iteritems()]


def triangular_solve(rowlist, b, label_list):
    """
    Input: rowlist -> a list of row Vectors all w/ same finite domain D.
           b -> a list of the same length as each Vector containing numbers.
           label_list -> a list consisting of all the elements of D.

    Output: x -> a Vector s.t for i in [1,..,n-1], the dot product
                 of rowlist[i] and x equals b.
    """
    D = rowlist[0].D
    x = zero_vector(len(D))

    for j in reversed(range(len(D))):
        c = label_list[j]
        row = rowlist[j]
        x[c] = (b[j] - x * row) / row[c]
    return x
