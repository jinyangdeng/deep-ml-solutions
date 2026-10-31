import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	def sigmoid(z):
		return 1/(1+np.exp(-z))
	
	updated_weights = initial_weights.copy()
	updated_bias = initial_bias
	mse_values = []

	num_classes = len(labels)

	for _ in range(epochs):
		z = features @ updated_weights + updated_bias
		pred = sigmoid(z)
		err = pred - labels
		mse_values.append(1/num_classes * np.sum(np.power(err, 2)))

		dloss_dpred = 2/num_classes * err * 1
		dpred_dz = pred * (1 - pred)
		dloss_dz = dloss_dpred * dpred_dz
		updated_bias -= learning_rate * dloss_dz.sum()
		updated_weights -= learning_rate * (features.T @ dloss_dz) 
	
	return updated_weights, updated_bias, mse_values