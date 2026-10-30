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

		for i in range(k + 1, num_rows):
			m_ik = A[i, k] / A[k, k]
			for j in range(k, num_cols):
				A[i, j] -= m_ik * A[k, j]
			b[i] -= m_ik * b[k]

	for k in range(num_rows - 1, -1, -1):
		for i in range(k + 1, num_rows):
			b[k] = b[k] - A[k, i] * b[i]
		b[k] = b[k] / A[k, k]
	return b


