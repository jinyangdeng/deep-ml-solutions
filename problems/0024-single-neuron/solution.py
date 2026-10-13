import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities = []
	for record in features:
		x = sum(f * w for f, w in zip(record, weights)) + bias
		probabilities.append(1/(1+math.exp(-x)))
	mse = 1/len(probabilities) * sum((l - p) ** 2 for l, p in zip(labels, probabilities))
	return probabilities, mse