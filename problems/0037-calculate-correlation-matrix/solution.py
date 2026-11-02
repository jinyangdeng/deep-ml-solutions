import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
	if Y is None:
		# Per https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html:
		# x: A 1-D or 2-D array containing multiple variables and observations. Each row of x represents a variable, and each column a single observation of all those variables.
		# Here, each column of X represents a variable, and each row is a single observation of all those variables
		# i.e. it's the other way round, so transpose
		return np.corrcoef(X.T)

	num_features = X.shape[1]
	return np.corrcoef(X.T, Y.T)[:num_features, num_features:]