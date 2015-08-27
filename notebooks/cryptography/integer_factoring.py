#!/usr/bin/python3

from core.vector import Vector

from util.factoring_util import dummy_factor
from util.factoring_util import intsqrt


# find integers a and b s.t. a**2 + b**2 = N

def root_method(N):
    """ Finds two integers a and b s.t. a**2 - b**2 == N.
    """
    a = intsqrt(N) + 1
    if type(intsqrt(a**3 - N)) == int:
        b = intsqrt(a**2 - N)
        return a - b


if __name__ == '__main__':

    pass
