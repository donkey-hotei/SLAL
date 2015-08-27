"""
Row Reduce Echelon Form

thanks to http://elonen.iki.fi/code/misc-notes/python-gaussj/
for the simple algorithm used in the guass_jordan function
"""
from matrixutil import matrix2rowdict, identity, coldict2matrix

# First Attempts at implementing row reduction


def rref(A):
    """
    Input: A -> a Matrix
    Output: echelon_A -> the Matrix A put into echelon form
    """
    rowlist = matrix2rowdict(A)  # matrix as row vectors
    M_rowlist = identity(A.D[1], 1)  # same sq. domain as A
    column_label_list = sorted(rowlist[0].D, key=str)  # decide on an ordering
    new_M_rowlist = []
    rows_left = set(range(len(rowlist)))
    for c in column_label_list:
        rows_with_nonzero = [r for r in rows_left if rowlist[r][c] != 0]
        if rows_with_nonzero != []:  # if there is a pivot point
            pivot = rows_with_nonzero[0]  # pivot at the first nonzero row
            rows_left.remove(pivot)
            new_M_rowlist.append(M_rowlist[pivot])
            for r in rows_with_nonzero[1:]:
                multiplier = rowlist[r][c] / rowlist[pivot][c]
                rowlist[r] -= multiplier * rowlist[pivot]
                M_rowlist[r] -= multiplier * M_rowlist[pivot]
        for r in rows_left:
            new_M_rowlist.append(M_rowlist[r])
    echelon_A = coldict2matrix(new_M_rowlist)
    return echelon_A


def row_reduce(rowlist):
    """
    Input: rowlist -> a Matrix represented as a list of row vectors
    Output: new_rowlist -> a Matrix in row reduced form
                           as a list of row vectors
    """
    col_label_list = sorted(  # decide on an ordering
        rowlist[0].D, key=str)
    # we'll represent a matrix as a list of row vectors
    # initialiing a set of vectors not yet transformed
    rows_left = set(range(len(rowlist)))
    new_rowlist = []
    # the algorithm will iterate thru the column labels in order.
    for c in col_label_list:
        # among the rows left, list of row-lavels whose rows have a nonzero
        # position at c
        rows_with_nonzero = [r for r in rows_left if rowlist[r][c] != 0]
        if rows_with_nonzero != []:
            pivot = rows_with_nonzero[0]  # selects one of the rows
            rows_left.remove(pivot)
            # and adds it to the new rowlist
            new_rowlist.append(rowlist[pivot])
            for r in rows_with_nonzero[1:]:
                rowlist[r] -= \
                    (rowlist[r][c] / rowlist[pivot][c]) * rowlist[pivot]
    return new_rowlist


def guass_jordan(m, epsilon=1.0 / (10**10)):
    """
    Puts the matrix into the Reduced Row Echelon Form.
    Returns True if sucessful, False if the matrix is singular.
    """
    return NotImplementedError


if __name__ == '__main__':
    from matrixutil import listlist2matrix
    A = listlist2matrix([[2, 0, 9],
                         [1, 2, 2],
                         [3, 5, 3]])
    print(A)
    print(matrix2rowdict(A))
    for v in matrix2rowdict(A).keys():
        print(matrix2rowdict(A)[v])

    print(row_reduce(matrix2rowdict(A)))
