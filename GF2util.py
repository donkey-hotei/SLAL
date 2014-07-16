"""
SLAL: Matrix/Vector Utility Functions
"""
from vector import Vector
from matrix import Matrix
from GF2 import zero, one

from vectorutil import linear_comb
# constructing the span of a set of vectors over GF2
# NOT FINISHED? If you can find a solution... will you?
def GF2_span(veclist):
    """ Returns the set of all linear combinations of the vectors in vectorset."""
    
    for 
        span = { veclist[d] * veclist[d+1] for vector in veclist }
    return span
    
def linear_comb(clist, vlist):
    
