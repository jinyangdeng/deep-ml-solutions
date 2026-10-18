import numpy as np

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	def recursive_determinant(inner_matrix):
		if len(inner_matrix) == 2:
			return inner_matrix[0][0] * inner_matrix[1][1] - inner_matrix[1][0] * inner_matrix[0][1]
		else:
			res = 0
			n = len(inner_matrix)
			# Choose row i = 0
			for j in range(len(inner_matrix)):
				res += (-1) ** (j) * inner_matrix[0][j] * recursive_determinant([row[:j] + row[j+1:] for row in inner_matrix[1:]]) 
			return res

	return (recursive_determinant(matrix), sum(matrix[i][i] for i in range(len(matrix))))