```
 ___  __      __    __   
/ __)(  )    /__\  (  )  
\__ \ )(__  /(__)\  )(__ 
(___/(____)(__)(__)(____)
```
Sparse Linear Algebra Library is
a simple library written in pure-python for exploring problems in linear algebra.
This library is meant for educational purposes only, and the lousy developer who created
this software is not responsible for any engineering mishaps that occur due to the use
of this library. 
You may be wondering why anyone would write a linear algebra library on their own when so many other, and better, libraries exist for the same purpose. The main reason is that I wanted to learn some linear algebra and being able to tell a machine how to operate  is an excellent litmus test for one's own knowledge of the subject.  
http://en.wikipedia.org/wiki/Not_invented_here

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
