import numpy as np

# Getting the user's input for the augmented matrix
print("Please enter the augmented matrix...")
matrix = np.array(eval(input("Ex: [[3, 1, -4, 7], [-2, 3, 1, -5], [2, 0, 5, 10]]: ")))

# Defining the Gaussian function to solve the system using Gaussian elimination with partial pivoting
def gaussian(A):
    n = A.shape[0]  # Number of rows
    for i in range(n - 1):
        # Selecting the pivot
        p = i
        # Comparison to select the pivot
        for j in range(i + 1, n):
            if abs(A[j, i]) > abs(A[i, i]):
                # Swapping rows if there's a bigger pivot
                U = A[i, :].copy()  # Store the current row temporarily
                A[i, :] = A[j, :]  # Swap rows
                A[j, :] = U  # Restore the row to the previous position

        # Check if the pivot is zero and adjust
        while A[p, i] == 0 and p < n:
            p += 1
        if p == n:
            print("No solution")
            return None

        if p != i:
            # Swap rows if necessary
            T = A[i, :].copy()  # Temp value for the current row
            A[i, :] = A[p, :]
            A[p, :] = T

        # Elimination process
        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]  # Multiplier to eliminate leading coefficient
            for k in range(i + 1, n + 1):
                A[j, k] -= m * A[i, k]  # Eliminating the leading coefficient

    # Check if there's no unique solution
    if A[n - 1, n - 1] == 0:
        print("No unique solution")
        return None

    # Back-substitution to solve for x
    x = np.zeros(n)
    x[n - 1] = A[n - 1, n] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sumax = 0
        for j in range(i + 1, n):
            sumax += A[i, j] * x[j]
        x[i] = (A[i, n] - sumax) / A[i, i]
    return x

# Calling the Gaussian function with the augmented matrix as the parameter
x = gaussian(matrix)

# Displaying the solution
if x is not None:
    print("The solution for this matrix is:", x)