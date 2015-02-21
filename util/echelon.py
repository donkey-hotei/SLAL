"""
Row Reduce Echelon Form 

thanks to http://elonen.iki.fi/code/misc-notes/python-gaussj/ 
for the simple algorithm used in the guass_jordan function
"""
from matrixutil import matrix2rowdict, identity, coldict2matrix

# First Attempts at implementing row reduction
def rref(A):
	"""
	Takes a matrix and returns it's reduced row echelon form.
	"""
	# We'll represent a matrix as a list of row vectors . 
	rowlist = matrix2rowdict(A)
	M_rowlist = identity(A.D[1], 1) # create an identity matrix with the same square domain as A
	# to handle vectors with an arbitrary domain, we must decide on an ordering
	column_label_list = sorted(rowlist[0].D, key=str)
	# first attempt at transforming a rowlist into one that is in echelon form
	# sort the rows by the position of the leftmost entry
	new_rowlist = [ ]
	new_M_rowlist = [ ]
	rows_left = set(range(len(rowlist)))
	# algorithm will itereate through the column labels in order .
	# in each iteration the algorithm finds a list rows_with_nonzero from the rows with nonzero entries
	# rows that have nonzero entries in the current column
	# The algorithm will then select one of these rows (the pivot row) and adds it to the new_rowlist,
	# and removes it from rows_left
	for c in column_label_list:
		rows_with_nonzero = [ r for r in rows_left if rowlist[r][c] != 0 ]
		if rows_with_nonzero != [ ]: # if the matrix was not a zero matrix
			pivot = rows_with_nonzero[0]
			rows_left.remove(pivot)
			new_M_rowlist.append(M_rowlist[pivot])
			for r in rows_with_nonzero[1:]:
				multiplier = rowlist[r][c] / rowlist[pivot][c]
				rowlist[r] -= multiplier * rowlist[pivot]
				M_rowlist[r] -= multiplier*M_rowlist[pivot]
		for r in rows_left:
			new_M_rowlist.append(M_rowlist[r])
	print(new_M_rowlist)
	new_A = coldict2matrix(new_M_rowlist)
	return new_A


def row_reduce(rowlist):
	"""
	Given a list of vectors, transforms the vectors, 
	Mutates the arguement. 
	Returns a list of nonzero reduced vectors, such that the matrix made 
	of them is in row reduced form.
	"""
	col_label_list = sorted(rowlist[0].D, key=str) # we'll represent a matrix as a list of row vectors 
	rows_left = set(range(len(rowlist))) # initialiing a set of vectors not yet transformed
	new_rowlist = [ ]
	for c in col_label_list: # the algorithm will iterate thru the column labels in order.
		# among the rows left, list of row-lavels whose rows have a nonzero position at c
		rows_with_nonzero = [ r for r in rows_left if rowlist[r][c] != 0 ]
		if rows_with_nonzero != [ ]:
			pivot = rows_with_nonzero[0] # selects one of the rows
			rows_left.remove(pivot) 
			new_rowlist.append(rowlist[pivot]) # and adds it to the new rowlist
			for r in rows_with_nonzero[1:]:
				rowlist[r] -= (rowlist[r][c] / rowlist[pivot][c]) * rowlist[pivot]
	return new_rowlist




def guass_jordan(m, epsilon = 1.0/(10**10)):
	"""
	Puts the matrix into the Reduced Row Echelon Form.
	Returns True if sucessful, False if the matrix is singular.
	"""
	return NotImplementedError 


if __name__ == '__main__':
	from vectorutil import list2vector
	from matrixutil import listlist2matrix, matrix2rowdict, coldict2matrix, identity
	A = listlist2matrix([[2, 0, 9],
			     [1, 2, 2],
			     [3, 5, 3]])
	print(A)
	print(matrix2rowdict(A))
	for v in matrix2rowdict(A).keys():
		print(matrix2rowdict(A)[v])

	print(row_reduce(matrix2rowdict(A)))
