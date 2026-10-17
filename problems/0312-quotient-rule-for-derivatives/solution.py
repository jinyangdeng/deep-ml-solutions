import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    if x == 0:
        return -1
    g_coeffs.reverse()
    h_coeffs.reverse()

    g_x = 0
    for idx, coeff in enumerate(g_coeffs):
        g_x += (coeff * (x ** idx))
    
    h_x = 0
    for idx, coeff in enumerate(h_coeffs):
        h_x += (coeff * (x ** idx))
    
    g_p_x = 0
    for idx, coeff in enumerate(g_coeffs):
        g_p_x += (coeff * idx * (x ** (idx - 1)))

    h_p_x = 0
    for idx, coeff in enumerate(h_coeffs):
        h_p_x += (coeff * idx * (x ** (idx - 1)))
    
    return (g_p_x * h_x - g_x * h_p_x) / (h_x ** 2)
    