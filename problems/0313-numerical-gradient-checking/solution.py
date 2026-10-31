import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    n = len(analytical_grad)
    numerical_grad = np.zeros(n)
	
    for x_i in range(n):
        x[x_i] += epsilon
        f_plus_h_dx = f(x)
        x[x_i] -= 2 * epsilon
        f_minus_h_dx = f(x)
        j_x = (f_plus_h_dx - f_minus_h_dx) / (2 * epsilon)
        numerical_grad[x_i] = j_x
        x[x_i] += epsilon
	
    diff = numerical_grad - analytical_grad
    sum_of_norms = np.linalg.norm(numerical_grad) + np.linalg.norm(analytical_grad)

    # relative_error = ||numerical_grad - analytical_grad|| / (||numerical_grad|| + ||analytical_grad||)
    relative_error = np.linalg.norm(diff) / sum_of_norms if sum_of_norms != 0 else 0
    return (numerical_grad, relative_error)