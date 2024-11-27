import numpy as np
from global_functions_and_more.sort_and_dominant import sort, dominant

def ant_seidel(user_matrix_a, matrix_b, initial_guess, flag, tolerance=0.001):
    # Solve Ax = b using the Gauss-Seidel method
    matrix_a = sort(user_matrix_a)
    matrix_a = dominant(matrix_a)
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
            case "a":
                errors = abs(x - old_x)  # Mean Absolute Error
                if np.mean(errors) < tolerance:
                    break
            case "b":
                errors = np.sqrt((x - old_x) ** 2)  # Root Mean Square Error
                if np.mean(errors) < tolerance:
                    break
            case "c":
                errors = abs(np.dot(matrix_a, x) - matrix_b)  # True MAE
                if np.mean(errors) < tolerance:
                    break
            case "d":
                errors = np.sqrt((np.dot(matrix_a, x) - matrix_b) ** 2)  # True RMSE
                if np.mean(errors) < tolerance:
                    break
    return x  # Return the computed solution