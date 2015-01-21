"""

 ___  __      __    __   
/ __)(  )    /__\  (  )  
\__ \ )(__  /(__)\  )(__ 
(___/(____)(__)(__)(____)



SLAL: Sparse Linear Algebra Library
(c)opyleft : free software
dynsne 
"""
from core.vector import Vector 

class Matrix:
    """
    A Matrix has two fields:
    D - the domain (a tuple of two sets, the first is the row domain, second in column domain
    f - a dictionary mapping some of elements in the domain to a field,
        follows the sparsity convention of the Vector class
    """
    def __init__(self, labels, function):
        self.D = labels
        self.f = function
        rows = labels[0]
        columns = labels[1]

    def __getitem__(self,k):
        return 0 if k not in self.f else self.f[k]
        
    def __setitem__(self, k, val): self.f[k] = val

    def transpose(self):
        return Matrix((self.D[1], self.D[0]), {c : r for (r, c) in self.f.keys()}) 

    def __neg__(self):
        return (-1)*self

    # There's something up with the polymorhphism here...
    def __mul__(self,other):
        if Matrix == type(other): # matrix-matrix
            assert self.D[1] == other.D[0]
            result_matrix = Matrix((self.D[0],other.D[1]), {})
            for r in self.D[0]:
                for c in other.D[1]:
                    result_matrix[r,c] = sum([self[r,k] * other[k,c] for k in other.D[1]])
            return result_matrix

        # for some reason matrix-vector multiplication yields type None
        elif Vector == type(other): # matrix-vector
            assert other.D == self.D[1]
            result_vector = Vector( self.D[0], {})
            for (i, j) in self.f.keys():
                result_vector[j] += self[i,j] * other[j]
            return result_vector
  
        elif type(other) == int or type(other) == float:
            # scalar-matrix
            result_matrix = Matrix((self.D[0], self.D[1]), {})
            for (i, j) in self.f.keys():
                result_matrix[i,j] += self[i, j] * other
            return result_matrix
                        
        #this will only be used if other is scalar (or not-supported). matrix and vector both have __mul__ implemented

    def __rmul__(self, other):
        if Vector == type(other): # vector-matrix
            assert other.D == self.D[0]
            result_vector = Vector(other.D, {c : self[r, c] * other[c]
                                             for (r, c) in self.f.keys()})
                    
            return result_vector
        else:  # Assume scalar
            result_matrix = Matrix( (self.D[0], self.D[1]),
                                    {(r, c) : other*self[r,c]
                                    for (r, c) in self.f.keys() } )
            return result_matrix


    # addition of matrices was easy enough
    def __add__(self, other):
        assert type(other) == Matrix
        assert self.D[1] == other.D[1] 
        result_matrix = Matrix((self.D[0], self.D[1]),
                               {(r, c) : self[r, c] + other[r, c]
                               for r in self.D[0] for c in self.D[1]})
        return result_matrix
        
    def __sub__(a,b):
        return a+(-b)

    def __eq__(self, other):
        return NotImplementedError

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None: rows = sorted(M.D[0], key=repr) 
        if cols == None: cols = sorted(M.D[1], key=repr)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec))
                                              if isinstance(M[row,col], int)
                                              or isinstance(M[row,col], float)
                                              else len(str(M[row,col]))
                                              for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec)
                                                                       if isinstance(M[r,c], int)
                                                                       or isinstance(M[r,c], float)
                                                                       else '{0:>{1}}'.format(M[r,c], colw[c])
                                                                       for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4
    
    def prettyprint(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Matrix(" + str(self.D) +", " + str(self.f) + ")"

