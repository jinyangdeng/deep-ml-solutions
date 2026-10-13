import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    ids = list(range(n_samples))
    if shuffle:
        np.random.shuffle(ids)
    test_ranges = [[0, n_samples // k + n_samples % k]]
    while test_ranges[-1][-1] != n_samples:
        test_ranges.append([test_ranges[-1][1], test_ranges[-1][1] + n_samples // k])
    res = []
    for test_range in test_ranges:
        res.append(([e for e in ids if e not in set(ids[test_range[0]:test_range[1]])], ids[test_range[0]:test_range[1]]))
    return res
