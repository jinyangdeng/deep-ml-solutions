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
	# Note that np.corrcoef(X.T, Y.T) wouldn't work right away, because numpy's implementation for corrcoef is not what we thought
	# We wish for cross-correlation.
	# But Numpy is actually stacking X.T and Y.T vertically (i.e. we are introducing more variables for each observation)
	# As such, the correlation matrix is now
	#     x_1 | x_2 | y_1 | y_2
	# x_1 
	# x_2
	# y_1
	# y_2 
	# By [:num_features, num_features:], we take the right upper corner.
	# (The bottom-left [num_features:, :num_features] block is its transpose: rows y, cols x.)
	return np.corrcoef(X.T, Y.T)[:num_features, num_features:]