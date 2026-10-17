import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type == "l1":
        return np.float32(np.sum(np.abs(arr)))
    elif norm_type == "l2":
        return np.sqrt(np.sum(np.power(arr, 2)))
    elif norm_type == "linf":
        return np.float32(np.max(np.abs(arr)))
    elif norm_type == "frobenius":
        if np.ndim(arr) != 2:
            raise ValueError()
        return np.sqrt(np.sum(np.power(arr, 2)))
