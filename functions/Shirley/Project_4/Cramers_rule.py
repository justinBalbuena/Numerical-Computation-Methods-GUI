import numpy as np

def Cramers_rule(matrix_a):
    #getting the number of rows and columns of the augmented matrix
    r, c = matrix_a.shape
    #ensuring that matrix is an augmented matrix (r rows, r+1 columns)
    if c != r + 1:
        raise ValueError("The input matrix is not an augmented matrix.")
    #seperating the coefficient matrix (A) and the constant vector (b)
    A = matrix_a[:, :-1]  #coefficients matrix
    b = matrix_a[:, -1]  #constants vector
    #checking if the coefficient matrix is singular (det(A) == 0)
    det_A = np.linalg.det(A)
    if np.abs(det_A) < 1e-10:
        raise ValueError("The determinant of the coefficient matrix is zero, so the system is singular.")
    #initializing the solution vector
    solution = np.zeros(r)
    # applying Cramer's Rule
    for i in range(r):
        # creating a copy of A and replace the i-th column with the constant vector b
        temp_matrix = A.copy()
        temp_matrix[:, i] = b
        # Computing the determinant of the modified matrix and calculate the solution
        solution[i] = np.linalg.det(temp_matrix) / det_A
    return solution