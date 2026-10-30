import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	num_rows, num_cols = A.shape
	for k in range(0, num_rows - 1):
		# Apply partial pivoting
		# From k-th row onwards, which row has the max abs val in k-th column?
		pivot_row = k + np.argmax(np.abs(A[k:, k]))
		# I switch place between k-th row and pivot_row
		# Note that it is very tempting to write A[k], A[pivot_row] = A[pivot_row], A[k], but that will corrupt the memory
		A[[k, pivot_row]] = A[[pivot_row, k]]
		b[[k, pivot_row]] = b[[pivot_row, k]]
		# A[k, k] is the max absolute value in column k
		
		# Now, use k-th row to remove any traces of k from the rows below it
		for i in range(k + 1, num_rows):
			m_ik = A[i, k] / A[k, k]
			# Cleaning up the entire row
			for j in range(k, num_cols):
				A[i, j] -= m_ik * A[k, j]
			b[i] -= m_ik * b[k]
	"""
	A will now look something like:
	[[ 4.  10.  -1. ]
	 [ 0.   3.   4.5]
	 [ 0.   0.   1.5]]
	B will look like [11. -4.  3.]
	"""
	# Back elimination
	for k in range(num_rows - 1, -1, -1):
		# 我从下往上走时，假设解开了 row 2， 现在在解 row 1: 3 * x1 + 4.5 * x2 = -4
		# 之前的 x2 已经求出来了，那就是在 b[2]，扣掉它
		for i in range(k + 1, num_rows):
			b[k] -= A[k, i] * b[i]
		# 现在: 3 * x1 = -4 - 4.5 * b[2]，把 3 移到右边即可
		b[k] = b[k] / A[k, k]
	return b


