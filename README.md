Sparse Linear Algebra Library
A simple library for exploring problems in linear algebra written in pure-python.
To try it out just clone the 

Matrix-Vector Multiplication 
```python
from matrix import Matrix
from vector import Vector
from matrixutil import listlist2matrix
from vectorutil import list2vector

>>> M = listlist2vector([[ 1, 1 ],
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
