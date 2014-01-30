"""
SLAL: Sparse Linear Algebra Library
by dysne
(c)opyleft

Matrix utility functions.
"""
from matrix import Matrix


# utility functions for matrices
def listlist2matrix(L):
    """ Turns a list of lists into a matrix. """
    rows = range(len(L))
    cols = range(len(L[0]))
    return Matrix( (set(rows),set(cols)), {(i, j) : L[i][j]
                                           for i in rows
                                           for j in cols })

# this one is broken .. grabbing the column domain isntead
# of the row domain
def matrix2rowlist(M):
    """
    Makes a list of vectors of the rows of a matrix.
    """
    rowlist = [ ]
    rows = M.D[0]
    cols = M.D[1]
    for row in rows:
        rowlist.append(Vector( rows, {c:M[(row, c)] for c in cols} ) )
    return rowlist

def matrix2columnlist(M):
    """
    Makes a list of vectors out of the columns of the matrix.
    """
    collist = [ ]
    rows = M.D[0]
    cols = M.D[1]
    for col in cols:
        collist.append(Vector( cols, {r:M[(r, col)] for r in rows}))
    return collist


def identity_matrix(M):
    """
    Creates an identity with the same domain as M
    """
    return Matrix(M.D, { (r, r) : 1 for (r, c) in M.f.keys()  })
    

