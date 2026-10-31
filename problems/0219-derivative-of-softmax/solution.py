import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	def f(x):
		return np.exp(x) / np.sum(np.exp(x))
	h = 1e-5
	# Your code here
	n = len(x)
	m = len(f(x))
	res = [[0] * n for i in range(m)]
	
	f_x = f(x)
	for x_i in range(n):
		x[x_i] += h
		f_x_dx = f(x)
		diff = [e1 - e2 for e1, e2 in zip(f_x_dx, f_x)]
		j_x = [d / h for d in diff]
		for idx, val in enumerate(j_x):
			res[idx][x_i] = val
		x[x_i] -= h
	
	return res