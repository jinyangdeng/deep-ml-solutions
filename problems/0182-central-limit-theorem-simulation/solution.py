import numpy as np

def simulate_clt(distribution: str, n: int, runs: int = 10000, seed: int = 42) -> dict:
    """
    Simulate the Central Limit Theorem.

    Args:
        distribution (str): The distribution to sample from ('uniform', 'exponential', 'bernoulli').
        n (int): Sample size.
        runs (int): Number of repeated experiments.
        seed (int): Random seed for reproducibility.

    Returns:
        dict: {'mean': float, 'std': float} of the standardized sample means.
    """
    np.random.seed(seed)
    # Your implementation here
    if distribution == "uniform":
        data = np.random.uniform(0, 1, size=(runs, n))
        mu, sigma = 0.5, np.sqrt(1/12)
    elif distribution == "exponential":
        data = np.random.exponential(1.0, size=(runs, n))
        mu, sigma = 1, 1
    elif distribution == "bernoulli":
        data = (np.random.rand(runs, n) < 0.3).astype(float)
        mu, sigma = 0.3, np.sqrt(0.3 * 0.7)

    means = (np.mean(data, axis=1) - mu) / (sigma / np.sqrt(n))
    return {'mean': np.mean(means), 'std': np.std(means)}
