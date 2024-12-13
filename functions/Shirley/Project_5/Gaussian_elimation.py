import numpy as np
from sympy import Matrix

def gaussian(augmented_matrix):
    # Convert input to numpy array to ensure compatibility
    A = np.array(augmented_matrix.tolist(), dtype=float)
    # Get number of rows and columns
    n = A.shape[0]
    # Perform Gaussian elimination with partial pivoting
    for i in range(n):
        # Find pivot row
        max_element = abs(A[i:, i]).argmax() + i
        # Swap maximum row with current row
        if max_element != i:
            A[[i, max_element]] = A[[max_element, i]]
        # Check for zero pivot
        if np.isclose(A[i, i], 0):
            # If pivot is effectively zero, matrix is singular
            return None
        # Eliminate below current row
        for j in range(i + 1, n):
            # Calculate multiplier
            factor = A[j, i] / A[i, i]
            # Subtract multiple of current row
            A[j, i:] -= factor * A[i, i:]

    # Back substitution
    x = np.zeros(n)
    # Solve from bottom row upwards
    for i in range(n - 1, -1, -1):
        # Calculate x[i]
        x[i] = (A[i, -1] - np.dot(A[i, i + 1:n], x[i + 1:n])) / A[i, i]

    return [round(val, 10) for val in x]