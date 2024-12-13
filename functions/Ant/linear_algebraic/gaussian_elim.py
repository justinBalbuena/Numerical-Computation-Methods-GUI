import numpy as np

# Defining the Gaussian function to solve the system using Gaussian elimination with partial pivoting
def gaussian_elimination(A):
    A = np.array(A, dtype=float)  # Ensure the input is a NumPy ndarray and of type float
    n = A.shape[0]  # Number of rows

    for i in range(n - 1):
        # Partial pivoting: Find the maximum element in the current column
        max_row = np.argmax(abs(A[i:, i])) + i
        if A[max_row, i] == 0:
            print("No unique solution: Singular matrix")
            return None

        # Swap rows if necessary
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]

        # Perform elimination
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]

    # Back substitution
    if A[n - 1, n - 1] == 0:
        print("No unique solution: Singular matrix")
        return None

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (A[i, -1] - np.dot(A[i, i + 1:n], x[i + 1:n])) / A[i, i]

    return x



