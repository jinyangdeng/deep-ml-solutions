import numpy as np

def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	# Your code here
	def softmax(logits):
		return np.exp(logits) / np.sum(np.exp(logits))

	one_hot = [0 for i in range(len(logits))]
	one_hot[target] = 1
	return np.subtract(softmax(logits), one_hot)