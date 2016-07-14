"""
Matrix utility functions.
"""
from core.Vector import Vector
from core.Matrix import Matrix


def efficient_rowdict2matrix(rowdict):
    col_labels = value(rowdict).D
    M = Matrix((set(keys(rowdict)), col_labels), {})
    for r in rowdict:
        for c in rowdict[r].f:
            M[r, c] = rowdict[r][c]
    return M


def identity(D, one):
    """Given a set D and the field's one, returns the DxD identity Matrix
    e.g.:

    >>> identity({0,1,2}, 1)
    Matrix(({0, 1, 2}, {0, 1, 2}), {(0, 0): 1, (1, 1): 1, (2, 2): 1})
    """
    return Matrix((D, D), {(d, d): one for d in D})


def keys(d):
    """
    Input: d -> a dictionary or list
    Output: an iterable of for keys

    Intended for use with coldict2matrix and rowdict2matrix.
    """
    return d.keys() if isinstance(d, dict) else range(len(d))


def value(d):
    """Given either a dict or a list, returns one of the values.
     Intended for coldict2matrix and rowdict2matrix.
    """
    return next(iter(d.values())) if isinstance(d, dict) else d[0]


def matrix2rowdict(A):
    """
    Input: A -> a Matrix
    Output: a dictionary mapping row labels of A to rows of A.
     e.g.:

     >>> M = Matrix(({0, 1, 2}, {0, 1}),
                 {(0, 1): 1, (2, 0): 8, (1, 0): 4, (0, 0): 3, (2, 1): -2})

     >>> matrix2rowdict(M)
     {0: Vector({0, 1},{0: 3, 1: 1}),
      1: ({0, 1},{0: 4, 1: 0}),
      2: Vector({0, 1},{0: 8, 1: -2})}

     >>> matrix2rowdict(Matrix(({0,1},{0,1}),{}))
     {0: Vector({0, 1},{0: 0, 1: 0}), 1: Vector({0, 1},{0: 0, 1: 0})}
     """
    return {row: Vector(A.D[1], {col: A[row, col]
                                 for col in A.D[1]}) for row in A.D[0]}


def matrix2coldict(A):
    """
    Input: A -> a Matrix
    Output: a dictionary mapping column labels to columns of A.

     e.g.:
     >>> M = Matrix(({0, 1, 2}, {0, 1}),
                {(0, 1): 1, (2, 0): 8, (1, 0): 4, (0, 0): 3, (2, 1): -2})

     >>> matrix2coldict(M)
     {0: Vector({0, 1, 2},{0: 3, 1: 4, 2: 8}),
      1: Vector({0, 1, 2},{0: 1, 1: 0, 2: -2})}

     >>> matrix2coldict(Matrix(({0,1},{0,1}),{}))
     {0: Vector({0, 1},{0: 0, 1: 0}), 1: Vector({0, 1},{0: 0, 1: 0})}
    """
    return {col: Vector(A.D[0], {row: A[row, col]
                                 for row in A.D[0]}) for col in A.D[1]}


def coldict2matrix(coldict):
    """
    Input: coldict -> a dictionary whose values are Vectors
    Output: a Matrix having those Vectortors as columns.

    If coldict is a dictionary then its keys will be the
    column-labels of the Matrix.
    If coldict is a list then {0...len(coldict)-1} will
    be the column-labels of the Matrix.
    e.g.:

    >>> A = {0:Vector({0,1},{0:1,1:2}),1:Vector({0,1},{0:3,1:4})}
    >>> B = [Vector({0,1},{0:1,1:2}),Vector({0,1},{0:3,1:4})]
    >>> matrix2coldict(coldict2matrix(A)) == A
    True
    >>> coldict2matrix(A)
    Matrix(({0, 1}, {0, 1}), {(0, 1): 3, (1, 0): 2, (0, 0): 1, (1, 1): 4})
    >>> coldict2matrix(A) == coldict2matrix(B)
    True
    """
    row_labels = value(coldict).D
    return Matrix((row_labels, set(keys(coldict))),
                  {(r, c): coldict[c][r]
                   for c in keys(coldict)
                   for r in row_labels})


def rowdict2Matrix(rowdict):
    """
    Input: rowdict -> a dictionary or list whose values are Vectors
    Output: a Matrix having these Vectors as its rows.

    Assumes all the Vectors have the same label-set.
    Assumes row_dict is nonempty.
    If rowdict is a dictionary then its keys will be the
    row-labels of the Matrix.
    If rowdict is a list then {0...len(rowdict)-1} will
    be the row-labels of the Matrix.
    e.g.:

    >>> A = {0:Vector({0,1},{0:1,1:2}),1:Vector({0,1},{0:3,1:4})}
    >>> B = [Vector({0,1},{0:1,1:2}),Vector({0,1},{0:3,1:4})]
    >>> matrix2rowdict(rowdict2Matrix(A)) == A
    True
    >>> rowdict2matrix(A)
    Matrix(({0, 1}, {0, 1}), {(0, 1): 2, (1, 0): 3, (0, 0): 1, (1, 1): 4})
    >>> rowdict2matrix(A) == rowdict2matrix(B)
    True
    """
    col_labels = value(rowdict).D
    return Matrix((set(keys(rowdict)), col_labels),
                  {(r, c): rowdict[r][c]
                   for r in keys(rowdict)
                   for c in col_labels})


def listlist2matrix(L):
    """
    Input: L -> a list of lists of field elements
    Output: a Matrix whose ith rows consists of the elements
            in the ith list.
            Row labels are {0..len(L)}, and the
            column labels are {0..len(L[0])}

    >>> A=listlist2Matrix([[10,20,30,40],[50,60,70,80]])
    >>> print(A)

          0  1  2  3
       -------------
    0  |  10 20 30 40
    1  |  50 60 70 80

    """
    m, n = len(L), len(L[0])
    return Matrix((set(range(m)), set(range(n))),
                  {(r, c): L[r][c]
                   for r in range(m)
                   for c in range(n)})


def is_orthogonal(A):
    """
    Input: A -> a Matrix
    Ouput: a boolean indicating whether the A is orthogonal.
    """
    # orthogonal iff A * A^T is the identity matrix
    return A * A.transpose() == identity(A.D)
