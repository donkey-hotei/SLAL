Sparse Linear Algebra Library
A simple library written in pure-python for exploring problems in linear algebra.
Runs only in Python3, not currently backwards compatatible. 


Matrix-Vector Multiplication 
```python
from matrix import Matrix
from vector import Vector
from matrixutil import listlist2matrix
from vectorutil import list2vector

>>> M = listlist2matrix([[ 1, 1 ],
                         [ 2, 3]])
>>> v = list2vector([1, 2])

>>> print(M)
       0 1
     -----
 0  |  1 1
 1  |  2 3

>>> print(v)
 0 1
----
 1 2

```
