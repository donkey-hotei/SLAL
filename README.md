Sparse Linear Algebra Library
A simple library written in pure-python for exploring problems in linear algebra.
This library is meant for educational purposes only, and the poor developer who created
this software is not responsible for any engineering mishaps that occur due to the use
of this library. 

Library is only compatible with Python3 or greater, not currently backwards compatatible. 

Tutorials are currently in the works.

TODO: 
	- Implement Gaussian Elimination 
	- Finish up Threshold secret sharing notebook

Matrix-Vector Multiplication 
```python
from SLAL.core.matrix import Matrix
from SLAL.core.vector import Vector
from SLAL.utils.matrixutil import listlist2matrix
from SLAL.utils.vectorutil import list2vector

>>> A = listlist2matrix([[ 1, 1 ],
                         [ 2, 3]])
>>> x = list2vector([1, 2])

>>> print(A)
       0 1
     -----
 0  |  1 1
 1  |  2 3

>>> print(x)
 0 1
----
 1 2
 
 >> print(M * v)
 0 1
----
 3 8  


```
