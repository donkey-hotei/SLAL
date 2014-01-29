"""
SLAL: Matrix/Vector Utility Functions
"""
from vector import Vector
from matrix import Matrix
from GF2 import zero, one

from vectorutil import linear_comb
# constructing the span of a set of vectors over GF2
def GF2_span(labels, veclist):
    """ Returns the set of all linear combinations of the vectors in vectorset."""
    span = {}
    # endeavoring to use a comprehension within a loop
