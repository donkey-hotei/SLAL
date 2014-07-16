"""
SLAL: Utility functions for working over Galois Field 2
"""
from random import choice
from itertools import combinations, chain

from vector import Vector
from matrix import Matrix
from GF2 import zero, one


def GF2_span(veclist:list)->set:
    """ Returns the set of all linear combinations of the vectors in vectorset."""
    possible_coeffs = powerset
    for coeffs in possible_coeffs:
    
def linear_comb(clist:list, vlist:list)->Vector:
    """
    Returns a linear combination of the vectors in vlist
    with the corresponding coefficients in clist.
    """
    assert len(clist) == len(vlist)
    return sum([ coeff * vec for (coeff, vec) in zip(clist, vlist) ])

def powerset(coeffs:set)->list:
    """
    Gives all the possible n-length subset combinations of a set.
    """
    powerset = [ ]
    for z in chain.from_iterable(combinations(coeffs, r) for r in range(len(coeffs)+1)):
        powerset.append(z)
    return powerset
