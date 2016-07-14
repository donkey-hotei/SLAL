#!/usr/bin/python
"""
QR Factorization
This is a decomposition of a matrix A into
the product A = QR, where Q is some orthogonal
matrix and R is an upper trianglular matrix.

If the first n columns of A are linearly independent,
then the first n columns of Q make up an orthonormal
basis for the column space of A.
"""

from orthonormalization import aug_orthonormalize
from dictutil import dict2list, list2dict
from matrixutil import matrix2coldict, coldict2mat


def factor(A):
    """ Implementation of the Gram-Schmidt procedure.
    """
    col_labels = sorted(A.D[1], key=hash)
    Acols = dict2list(matrix2coldict(A), col_labels)
    Qlist, Rlist = aug_orthonormalize(Acols)
    # Now make Matrices
    Q = coldict2mat(Qlist)
    R = coldict2mat(list2dict(Rlist, col_labels))
    return Q, R
