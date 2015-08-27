#!/usr/bin/python3

from core.vector import Vector
from core.GF2 import one, zero

from util.factoring_util import dumb_factor, intsqrt, primes, prod


def int2GF2(integer):
    """ Convert integer to a binary one or zero.
    """
    return zero if integer % 2 == 0 else one


def make_Vector(primeset, factors):
    """ Input: a set of primes and a list of factors.
        Output: a primeset-Vector over GF2 with domain primeset s.t
                v[p_i] == int2GF2(a_i) for i = 1, ..., s
    """
    vector = Vector(primeset, {})
    # all exponents mod 2
    for prime, factor in factors:
        vector[prime] = int2GF2(factor)
    return vector


# the results of find_candiates can be used to find a non-trivial
# divisor of N.


def find_canidates(N, primeset):
    """ Input: N -> integer to factor
               primtset -> set of primes
        Output: roots -> a list of size len(primset)+1 containing
                         integers a_i s.t. a_i**2 - N can be factored
                         completely over the primset.
                rowlist -> a list of integers over GF2 s.t. each element
                           i corresponds to a factor a_i
    """
    roots = []
    rowlist = []
    i = 2
    len_roots = 0  # faster than len(roots)
    while len_roots != len(primeset) + 1:
        x = intsqrt(N) + i
        F = dumb_factor(x * x - N, primeset)
        if F != []:
            roots.append(x)
            rowlist.append(make_Vector(primeset, F))
            len_roots += 1
        i += 1
    return roots, rowlist


def find_a_and_b(v, roots, N):
    """ Input: v -> a Vector over GF2
               roots -> a list of roots of N
               N -> the large integer to factor
    """
    alist = [root for root in roots if v[root] != zero]
    a = prod(alist)
    c = prod([(x * x - N) for x in alist])
    b = intsqrt(c)
    assert b * b == c
    return a, b


if __name__ == '__main__':
    from util.echelon import row_reduce

    # a**2 + b**2 == N
    # => (a+b) * (a-b) == N
    N = 2461799993978700679
    primeset = primes(10000)
    roots, rowlist = find_canidates(N, primeset)
    M = row_reduce(rowlist)
