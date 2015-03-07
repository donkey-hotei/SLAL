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
		- A : a matrix with rows as features
		- b : a vector of actual diagnoses
		- w : hypothesis vector 

	Output:
		- fraction of vectors incorrectly classfied (decimal between [0,1])
	"""
	sigma = signum(A*w)
	return abs(sigma*b) / len(b.D)  

def loss(A, b, w):
	"""
	Input:
		- A : a feature matrix 
		- b : diagnoses vector 
		- w : hypothesis vector 

	Output:
		- Value of loss function at w for traning data 
	"""
	return (A*w - b)**2 

def find_gradient(A, b, w):
	"""
	Input:
		- A : a feature matrix
		- b : diagnoses vector
		- w : hypothesis vector 

	Output:
		- value of gradient at w 
	"""
	return 2 * (A*w - b) 

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
	import random 
	A, b = read_training_data('train.data')
	w = Vector(A.D[1], {k : random.choice([1,-1]) for k in A.D[1]})
	print("Fraction incorrect with current vector w: %s" % fraction_wrong(A, b, w))

