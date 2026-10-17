import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	if set(gradient) == set([0]):
		return {
			"magnitude": 0,
			"direction": [0] * len(gradient),
			"descent_direction": [0] * len(gradient)
		}
	
	magnitude = np.linalg.norm(gradient)
	return {
		"magnitude": magnitude,
		"direction": np.divide(gradient, magnitude),
		"descent_direction": -np.divide(gradient, magnitude)
	}