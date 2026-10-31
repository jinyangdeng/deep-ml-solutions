import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
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