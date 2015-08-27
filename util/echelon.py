"""
Row Reduction of a Matrix (represented as a list of row Vectors)
"""
from matrixutil import matrix2rowdict

# gaussian elimination


def row_reduce(rowlist):
    """
    Input: rowlist -> a Matrix represented as a list of row vectors
    Output: new_rowlist -> a Matrix in row reduced form
                           as a list of row vectors
    """
    col_label_list = sorted(  # decide on an ordering
        rowlist[0].D, key=str)
    rows_left = set(range(len(rowlist)))
    echelon_rowlist = []
    for c in col_label_list:
        rows_with_nonzero = [r for r in rows_left if rowlist[r][c] != 0]
        if rows_with_nonzero != []:
            pivot = rows_with_nonzero[0]
            rows_left.remove(pivot)
            echelon_rowlist.append(rowlist[pivot])
            for r in rows_with_nonzero[1:]:
                rowlist[r] -= \
                    (rowlist[r][c] / rowlist[pivot][c]) * rowlist[pivot]
    return echelon_rowlist


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
