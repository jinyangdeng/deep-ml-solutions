def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	"""
	Calculate posterior probabilities using Bayes' Theorem.
	
	Args:
		priors: Prior probabilities P(H_i) for each hypothesis
		likelihoods: Likelihoods P(E|H_i) for each hypothesis
		
	Returns:
		Posterior probabilities P(H_i|E) for each hypothesis
	"""
	denom = sum(e1 * e2 for e1, e2 in zip(priors, likelihoods))
	return [e1 * e2 / denom for e1, e2 in zip(priors, likelihoods)]