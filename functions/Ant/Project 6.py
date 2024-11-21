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


def seidel(matrix_a, matrix_b, initial_guess, flag, tolerance=0.001):
    # Solve Ax = b using the Gauss-Seidel method
    n = matrix_a.shape[0]  # Number of rows
    x = initial_guess.copy()  # Initial guess for the solution

    while True:
        old_x = x.copy()
        errors = np.zeros(n)  # Store the previous iteration's values

        # Initialize error array
        for i in range(n):
            sum_a = sum(matrix_a[i, j] * x[j] for j in range(n) if j != i)  # Calculate x for current row
            x[i] = (matrix_b[i] - sum_a) / matrix_a[i, i]  # Update x[i] solution using the equation

        match flag:
            case 0:
                errors = abs(x - old_x)  # Mean Absolute Error
                if np.mean(errors) < tolerance:
                    break
            case 1:
                errors = np.sqrt((x - old_x) ** 2)  # Root Mean Square Error
                if np.mean(errors) < tolerance:
                    break
            case 2:
                errors = abs(np.dot(matrix_a, x) - matrix_b)  # True MAE
                if np.mean(errors) < tolerance:
                    break
            case 3:
                errors = np.sqrt((np.dot(matrix_a, x) - matrix_b) ** 2)  # True RMSE
                if np.mean(errors) < tolerance:
                    break
    return x  # Return the computed solution


def jacobi(matrix_a, matrix_b, initial_guess, flag, tolerance=0.001):
    # Solve Ax = b using the Jacobi method
    n = matrix_a.shape[0]  # Number of equations
    x = initial_guess.copy()  # Initial guess for the solution

    while True:
        old_x = x.copy()
        errors = np.zeros(n)  # Store the previous iteration's values

        # Initialize error array
        for i in range(n):
            sum_a = sum(matrix_a[i, j] * x[j] for j in range(n) if j != i)  # Calculate sum for current row
            x[i] = (matrix_b[i] - sum_a) / matrix_a[i, i]  # Update x[i] using the equation

        match flag:
            case 0:
                errors = abs(x - old_x)  # Mean Absolute Error
                if np.mean(errors) < tolerance:
                    break
            case 1:
                errors = np.sqrt((x - old_x) ** 2)  # Root Mean Square Error
                if np.mean(errors) < tolerance:
                    break
            case 2:
                errors = abs(np.dot(matrix_a, x) - matrix_b)  # True MAE
                if np.mean(errors) < tolerance:
                    break
            case 3:
                errors = np.sqrt((np.dot(matrix_a, x) - matrix_b) ** 2)  # True RMSE
                if np.mean(errors) < tolerance:
                    break
    return x  # Return the computed solution


# Example usage
matrix_a = np.array([[3, 1,-4, 7], [-2, 3, 1,-5], [2, 0, 5, 10]], float)
col = 4
row = 3
matrix_a = sort(matrix_a)  # Sort the matrix
matrix_a = dominant(matrix_a)  # Ensure dominant diagonal
matrix_b = matrix_a[:, col - 1]  # Extract the last column as b
matrix_a = np.delete(matrix_a, col - 1, 1)  # Remove last column from A
initial = np.array([0, 0, 0], float)  # Initial guess for the solution
print(matrix_a)
# Solve using the Jacobi method
roots = jacobi(matrix_a, matrix_b, initial, 1)
print(roots)  # Output the roots

[[3, 1,-4, 7], [-2, 3, 1,-5], [2, 0, 5, 10]]