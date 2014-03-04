"""
Implementation of Gaussian Elimination for SLAL
by dysnsne


thanks to http://elonen.iki.fi/code/misc-notes/python-gaussj/ 
for the simple algorithm used in the guass_jordan function
"""

def ref(A):
	"""
	Takes a matrix and returns it's reduced row echelon form.
	"""
	# We'll represent a matrix as a rowlist. 
	rowlist = matrix2rowlist(A)
	M_rowlist = identity(len(A.D[1]))
	# to handle vectors with an arbitrary domain, we must decide on an ordering
	column_label_list sorted(rowlist[0].D, key=str)
	# first attempt at transforming a rowlist into one that is in echelon form
	# sort the rows by the position of the leftmost entry
	new_rowlist = [ ]
	new_M_rowlist = [ ]
	rows_left = set(range(len(rowlist))))
	# algorithm will itereate through the column labels in order 
	# in each iteration the algorithm finds a list rows_with_nonzero of indices of the remaining
	# rows that have nonzero entries in the current column
	# The algorithm will then select one of these rows (the pivot row) and adds it to the new_rowlist,
	# and removes it from rows_left
	for c in column_label_list:
		rows_with_nonzero = [ r for r in rows_left if rowlist[r][c] != 0 ]
		if rows_with_nonzero != [ ]:
			pivot = rows_with_nonzero[0]
			rows_left.remove(pivot)
			new_M_rowlist.append(M_rowlist[pivot])
			for r in rows_with_nonzero[1:]:
				multiplier = rowlist[r][c] / rowlist[pivot][c]
				rowlist[r] -= multiplier * rowlist[pivot]
				M_rowlist[r] -= multiplier*M_rowlist[pivot]
		for r in rows_left:
			new_M_rowlist.append(M_rowlist[r])
	new_A = coldict2matrix(new_M_rowlist)
	return new_A


def guass_jordan(m, epsilon = 1.0/(10**10)):
	"""
	Puts the matrix into the Reduced Row Echelon Form.
	Returns True if sucessful, False if the matrix is singular.
	"""
	pass

