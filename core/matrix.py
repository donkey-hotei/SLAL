"""
 ___  __      __    __
/ __)(  )    /__\  (  )
\__ \ )(__  /(__)\  )(__
(___/(____)(__)(__)(____)
Sparse Linear Algebra Library
"""
from core.vector import Vector


class Matrix:

    """
    A Matrix has two fields:
    D - the domain (a tuple of two sets,
        the first is the row domain, second in column domain)
    f - a dictionary mapping some of elements in the domain to a field,
        follows a sparsity convention
    """

    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    def __getitem__(self, k):
        # this is the sparsity convention
        return 0 if k not in self.f else self.f[k]

    def __setitem__(self, k, val): self.f[k] = val

    def transpose(self):
        """ Returns transpose of Matrix """
        result = Matrix((self.D[1], self.D[0]), {})
        for i in self.D[0]:
            for j in self.D[1]:
                result[j, i] = self[i, j]
        return result

    def __neg__(self):
        return (-1) * self

    def __mul__(self, other):
        if Matrix == type(other):  # matrix-matrix
            assert self.D[1] == other.D[
                0], 'the number of rows in A should match' \
                ' the number of columns of B'
            result_matrix = Matrix((self.D[0], other.D[1]), {})
            for r in self.D[0]:
                for c in other.D[1]:
                    result_matrix[r, c] = sum(
                        [self[r, k] * other[k, c] for k in other.D[1]])
            return result_matrix

        elif Vector == type(other):  # matrix-vector
            assert other.D == self.D[1]
            return Vector(self.D[0],
                          {r: sum(self[r, c] * other[c]
                                  for c in self.D[1])
                           for r in self.D[0]})

        elif type(other) in [int, float]:
            # scalar-matrix
            result_matrix = Matrix((self.D[0], self.D[1]), {})
            for (i, j) in self.f.keys():
                result_matrix[i, j] += self[i, j] * other
            return result_matrix

    def __rmul__(self, other):
        if Vector == type(other):  # vector-matrix
            assert other.D == self.D[0]
            return Vector(self.D[1],
                          {c: sum(self[r, c] * other[r]
                                  for r in self.D[0])
                           for c in self.D[1]})

        else:  # otherwise we assume other is a scalar
            return Matrix((self.D[0], self.D[1]),
                          {(r, c): other * self[r, c]
                           for (r, c) in self.f.keys()})

    def __add__(self, other):
        assert type(other) == Matrix
        assert self.D[1] == other.D[1]
        result_matrix = Matrix((self.D[0], self.D[1]),
                               {(r, c): self[r, c] + other[r, c]
                                for r in self.D[0] for c in self.D[1]})
        return result_matrix

    def __sub__(a, b):
        return a + (-b)

    def __eq__(self, other):
        assert self.D == other.D
        return all([self[r, c] == other[r, c]
                    for r, c in zip(self.D[0], self.D[1])])

    def __pow__(self, power):
        """ Matrix exponentation """
        result_matrix = self
        for _ in range(power):
            result_matrix.__mul__(self)
        return result_matrix

    def copy(self):
        return Matrix(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        rows = sorted(M.D[0], key=repr)
        cols = sorted(M.D[1], key=repr)
        separator = ' | '
        numdec = 3
        pre = 1 + max([len(str(r)) for r in rows])
        colw = {col:
                (1 + max([len(str(col))]
                         + [len('{0:.{1}G}'.format(M[row, col], numdec))
                            if isinstance(M[row, col], int)
                            or isinstance(M[row, col], float)
                            else len(str(M[row, col]))
                            for row in rows])) for col in cols}
        s1 = ' ' * (1 + pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c, colw[c]) for c in cols])
        s3 = ' ' * (pre + len(separator)) + '-' * \
            (sum(list(colw.values())) + 1)
        s4 = ''.join(
            ['{0:>{1}} {2}'.format(r, pre, separator)
             + ''.join(['{0:>{1}.{2}G}'.format(M[r, c], colw[c], numdec)
                        if isinstance(M[r, c], int)
                        or isinstance(M[r, c], float)
                        else '{0:>{1}}'.format(M[r, c], colw[c])
                        for c in cols]) + '\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def prettyprint(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Matrix(" + str(self.D) + ", " + str(self.f) + ")"
