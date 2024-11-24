import numpy as np  # Import the NumPy library for numerical operations


def sort(matrix):
    # Sort the rows of the matrix based on the absolute values of the first column
    row, column = matrix.shape
    for i in range(row):
        for j in range(i + 1, row):
            if abs(matrix[j, i]) > abs(matrix[i, i]):
                matrix[[i, j], :] = matrix[[j, i], :]
    return matrix


def dominant(matrix):
    # Method to transform a non-diagonally dominant matrix to diagonally dominant
    row, column = matrix.shape
    D = np.diag(np.abs(matrix.copy()))  # Diagonal elements (absolute values) in a vector
    S = np.sum(np.abs(matrix.copy()), axis=1) - D  # Sum of non-diagonal elements to each row - the diagonal
    E = abs(matrix[:, column - 1])  # Last column (constant terms)

    for i in range(row - 1):
        # If the diagonal element is not greater than the sum of the row - matrix b
        if D[i] < S[i] - E[i]:
            for j in range(i + 1, row):
                if D[i] < matrix[j, i]:
                    matrix[i] += matrix[j]
                    break
    return matrix

