import numpy as np
import streamlit as st

# Gauss-Seidel function
def gauss_seidel(A_matrix, b, x, flag, tolerance):
    n = len(b)  # Number of rows
    old_x = np.copy(x)  # Store the previous iteration's solution
    error = float("inf")  # Initialize error with a large value
    while error > tolerance:  # Loop until the error is within tolerance
        for i in range(n):  # Iterate over rows
            x[i] = b[i]  # Initialize x[i] with b[i]
            for j in range(n):  # Iterate over columns
                if i != j:  # Skip the diagonal element
                    x[i] -= A_matrix[i, j] * x[j]  # Update x[i]
            x[i] /= A_matrix[i, i]  # Divide by the diagonal element
        # Compute error based on the stopping criterion
        if flag == 'a':  # Mean Absolute Error (MAE)
            errors = abs(x - old_x)
            error = np.mean(errors)
        elif flag == 'b':  # Root Mean Square Error (RMSE)
            errors = (x - old_x) ** 2
            error = np.sqrt(np.mean(errors))
        elif flag == 'c':  # True Mean Absolute Error (True MAE)
            errors = abs(np.dot(A_matrix, x) - b)
            error = np.mean(errors)
        elif flag == 'd':  # True Root Mean Square Error (True RMSE)
            errors = (np.dot(A_matrix, x) - b) ** 2
            error = np.sqrt(np.mean(errors))
        else:
            print("Invalid stopping criterion. Please choose between 0 and 3.")
        old_x = np.copy(x)  # Update old_x with the current solution
    return x  # Return the computed solution

# Check if matrix is diagonally dominant
def diag_dominant(A):
    n = A.shape[0]
    for i in range(n):
        row_sum = np.sum(np.abs(A[i, :])) - np.abs(A[i, i])  # Sum of non-diagonal elements
        if np.abs(A[i, i]) < row_sum:  # Check diagonal dominance
            return False
    return True

# Transform to diagonally dominant
def transform_dd(matrix):
    n = matrix.shape[0]
    for i in range(n):
        max_row_index = np.argmax(np.abs(matrix[i:, i])) + i
        if max_row_index != i:
            matrix[[i, max_row_index]] = matrix[[max_row_index, i]]  # Swap rows
    return matrix