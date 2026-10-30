import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Your code here
    A = np.array(A, dtype=float)
    num_rows, num_cols = A.shape
    for k in range(0, num_rows - 1):
        # Apply partial pivoting
        # From k-th row onwards, which row has the max abs val in k-th column?
        pivot_row = k + np.argmax(np.abs(A[k:, k]))
        # I switch place between k-th row and pivot_row
        # Note that it is very tempting to write A[k], A[pivot_row] = A[pivot_row], A[k], but that will corrupt the memory
        A[[k, pivot_row]] = A[[pivot_row, k]]
        # A[k, k] is the max absolute value in column k

        # Now, use k-th row to remove any traces of k from the rows below it
        for i in range(k + 1, num_rows):
            m_ik = A[i, k] / A[k, k]
            # Cleaning up the entire row
            for j in range(k, num_cols):
                A[i, j] -= m_ik * A[k, j]

    for i in range(num_rows):
        if np.all(np.abs(A[i]) <= tol):
            return i
    
    return num_rows
    