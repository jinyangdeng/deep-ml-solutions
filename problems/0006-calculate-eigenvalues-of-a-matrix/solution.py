def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	# A matrix turns one vector into another vector
	# For certain vectors, the matrix will only stretch them (& not turn them)
	# These stretch factors are eigenvalues
	# e.g. [[2, 1], [1, 2]] turns [1, 1] into [3, 3], so eigenvalue is 3
	# e.g. [[2, 1], [1, 2]] turns [1, -1] into [1, -1], so eigenvalue is 1
	# To find these eigenvalues, we try to solve the following
	# |2, 1| |x| = eigenvalue |x|
	# |1, 2| |y|              |y|
	# This becomes 2 equations: 
	# 1. 2x + y = eigenvalue x => (2 - eigenvalue)x + y = 0
	# 2. x + 2y = eigenvalue y => x + (2 - eigenvalue)y = 0
	# These equations can form the matrix | 2 - eigenvalue, 1 | |x| = |0|
    #                                     | 1, 2 - eigenvalue | |y|   |0|
	# Note that |x, y| cannot be |0, 0| because this is not a direction
	# As such,  | 2 - eigenvalue, 1 | also cannot have an inverse
	#           | 1, 2 - eigenvalue |
	# because suppose we call it M, M^-1 @ M = identity matrix, which will allow |x, y| to be |0, 0|
	# Since no inverse, means determinant (i.e. the product of main diagonal - product of other diagonal) is 0
	# Solving this: (2 - eigenvalue)(2 - eigenvalue) - 1 * 1 = 0 =>  eigenvalue^2 - 4 *  eigenvalue + 4 - 1 = 0
	# For a 2 by 2 matrix, this is eigenvalue^2 - trace * eigenvalue + determinant = 0
	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
	res = [(trace + (trace**2 - 4*det)**0.5)/2, (trace - (trace**2 - 4*det)**0.5)/2]
	return sorted(res, reverse=True)