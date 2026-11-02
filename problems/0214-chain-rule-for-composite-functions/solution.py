import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	ops = {
		"square": {
			"forward": lambda v: v ** 2,
			"backward": lambda v: 2 * v
		},
		"sin": {
			"forward": np.sin,
			"backward": np.cos
		},
		"exp": {
			"forward": np.exp,
			"backward": np.exp
		},
		"log": {
			"forward": np.log,
			"backward": lambda v: 1/v
		}
	}

	value, grad = x, 1
	for f in reversed(functions):
		op = ops[f]
		grad *= op["backward"](value)
		value = op["forward"](value)
	
	return grad