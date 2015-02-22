import sys
sys.path.append('../../')

from core.vector import Vector 
from core.matrix import Matrix
from cancer_data import read_training_data 

def signum(u):
	"""
	Input:
		- a Vector u

	Output:
		- the Vector v with the same domain as u s.t.
			v[d] == 1  if u[d] >= 0
			v[d] == -1 if u[d] < 0 

	Example:
		>>> signum(Vector({1,2,3},{1:2, 2:-1})) == Vector({1,2,3},{1:1,2:-1,3:1})
		True 
	"""
	v = Vector(u.D, {})
	for e in u.D:
		if u[e] >= 0: v[e] = 1
		else: v[e] = -1
	return v 

def fraction_wrong(A, b, w):
 	"""
	Input:	 
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
	Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly classified by w
	"""
	return signum(A*w) * b 


def loss(A, b, w):
	"""
	Input:
		- A : a feature matrix 
		- b : diagnoses vector 
		- w : hypothesis vector 

	Output:
		- Value of loss function at w for traning data 
	"""
	return NotImplementedError

def find_gradient(A, b, w):
	"""
	Input:
		- A : a feature matrix
		- b : diagnoses vector
		- w : hypothesis vector 

	Output:
		- value of gradient at w 
	"""
	return NotImplementedError

def gradient_descent_step(A, b, w, sigma):
	"""
	Input:
		- A : a feature matrix
		- b : a diagnoses vector
		- w : a hypothesis vector 
		- sigma : step size 

	Output:
		- The vector 'w' resulting from 1 iteration of gradient descent 
		  starting from w and moving sigma 
	"""
	return NotImplementedError

if __name__ == '__main__':
	print(signum(Vector({1,2,3},{1:2, 2:-1})) == Vector({1,2,3},{1:1,2:-1,3:1}))

