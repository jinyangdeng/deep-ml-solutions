import numpy as np
from collections import Counter

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    return {
        "mean": np.mean(data),
        "median": np.percentile(data, 50),
        "mode": Counter(data).most_common(1)[0][0],
        "variance": np.var(data),
        "standard_deviation": np.var(data) ** 0.5,
        "25th_percentile": np.percentile(data, 25),
        "50th_percentile": np.percentile(data, 50),
        "75th_percentile": np.percentile(data, 75),
        "interquartile_range": np.percentile(data, 75) - np.percentile(data, 25),
    }