import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Can just use https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html
	# Ord argument defaults to None, which mean L2
	# Implement your code here
	return v1 @ v2 / (np.linalg.norm(v1) * np.linalg.norm(v2))