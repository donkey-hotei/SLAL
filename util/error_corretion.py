"""
SLAL: Sparse Linear Algebra Library

Error Correcting Codes
"""

from vector import Vector
from matrix import Matrix
from GF2 import one, zero

from matrixutil import listlist2matrix
from matrixutil import matrix2coldict
from vectorutil import list2vector
import bitutil


# Hamming discovered a code in which a four bit message
# is represented by a seven-bit codeword.
# This generator matrix is:
G = listlist2matrix([[one, zero, one, one],
                     [one, one, zero, one],
                     [zero, zero, zero, one],
                     [one, one, one, zero],
                     [zero, zero, one, zero],
                     [zero, one, zero, zero],
                     [one, zero, zero, zero]])
# it is tradtional to define the generator matrix so that
# its rows are generators for C. We diverge from this
# tradition for the sake of simplicity.
print(G)
# After noting that the four rows of G are the standard
# basis vectors e1, ..., e4 we see that this implies a one-to-one
# relationship of uniqueness between words and codewords.
# Each word has a unique codeword to match it...
R = listlist2matrix([[zero, zero, zero, zero, zero, zero, one],
                     [zero, zero, zero, zero, zero, one, zero],
                     [zero, zero, zero, zero, one, zero, zero],
                     [zero, zero, one, zero, zero, zero, zero]])


# R = listlist2matrix([[one, one, zero, one, zero, zero, one],
#                     [zero, one, zero, one, zero, one, zero],
#                     [one, zero, zero, one, one, zero, zero],
#                     [one, one, one, zero, zero, zero, zero]])

# The [3,7] Hamming Matrix - how we find the posistion of the error
# Notice anythin special about the columns and their order?
# (From the left to the right they are counting in binary
H = listlist2matrix([[zero, zero, zero, one, one, one, one],
                     [zero, one, one, zero, zero, one, one],
                     [one, zero, one, zero, one, zero, one]])


def find_error(err):
    """
    input:-> the corrupted message err
    ouput:-> the error syndrome corresponding to err
    """
    position = sum([2**(i - 1) for i in err.f.keys() if err.f[i] == one]) - 1
    if position < 0:
        return Vector(err.D, {})
    else:
        return Vector(err.D, {position: one})

c_ = list2vector([one, zero, one, one, zero, one, one])
e = find_error(c_)
codeword = e + c_


def find_error_matrix(S):
    """
    input:-> a matrix S whose columns are error syndromes
    output:-> a matrix whose cth columns is the error corresponding
              to the cth column of S
    """
    columns = matrix2coldict(S)
    return coldict2matrix([find_error(columns[col]) for col in columns])

s = "I'm trying to free your mind Neo but I can only show you the door. You're the one who has to walk through it."


def str2matrix(text):
    """
    Computes a matrix over GF2 which represents the string passed in.
    """
    return bitutil.bits2matrix(bitutil.str2bits(text))
