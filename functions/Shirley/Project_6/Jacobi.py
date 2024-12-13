import numpy as np

def jacobi(A_matrix, tolerance, stop_c): #Jacobi function
    A = A_matrix[:, :-1] #everything excluding the augmented part of the matrix
    b = A_matrix[:, -1] #augmented part of the matrix
    n = len(b) #setting n equal to the length of augmented part of the matrix
    new_x = np.zeros(n) #creating a matrix of zeros to be updated
    x = np.ones(n)  #starting points
    if not diag_dominant(A_matrix[:, :-1]):  # if it is, then call the tranform_dd function
        A = transform_dd(A)
    for i in range(n): #going through the rows
        b[i] = b[i] / A[i, i] #changing b
        new_x[i] = x[i] #initial approximations
        for j in range(n): #growing through the rows
            if i != j:
                A[i, j] = A[i, j] / A[i, i] #non diagonal values are included
    error = float(10) #initializing error
    while error > tolerance: #will always run through unless error is less than the tolerance
        error = 0 #setting error equal to 0
        old_x = new_x.copy() #creating a copy of old_x
        for i in range(n): #going through the rows
            new_x[i] = b[i] #setting new_x equal to values of augmented part of the matrix
        for i in range(n): #going through the rows
            for j in range(n):
                if i != j: #if i is not equal to j
                    new_x[i] -= A[i, j] * old_x[j] #changing the current approximation
        if stop_c == 'a':  # Mean Absolute Error (MAE)
            error = np.mean(np.abs(x - old_x))
        elif stop_c == 'b':  # Root Mean Square Error (RMSE)
            error = np.sqrt(np.mean((x - old_x) ** 2))
        else:
            raise ValueError("Please choose 1 or 2.")  # Error message for invalid stop_c value

        if error < tolerance:  # Check if the error is within tolerance
            break
        error = error/n #approximate mean absolute error is a mean of sum of approximate absolute errors calculated for each unknown
    return new_x #returning newx

def diag_dominant(A): #checking if the matrix is diagonally dominant
    n = A.shape[0] #getting the size of the matrix
    for i in range(n): #iterating through the rows
        row_values = [] #creating a list to store the absolute values
        for j in range(n): #going through each column in the current row
            if j != i: #skipping over the diagonal element
                row_values.append(abs(A[i, j])) #appending the abs value of the off-diagonal element to the list
        row_sum = sum(row_values) #computing the sum of the absolute values in the row
        if abs(A[i, i]) < row_sum: #if absolute value of the diagonal element is less than the sum, continue
            return False #if it is not diagonally dominant return false
    return True #otherwise return true

def transform_dd(matrix):
    n = matrix.shape[0] #getting the size of the matrix
    for i in range(n):
        max_row_index = np.argmax(abs(matrix[i:, i])) + i #finding the row with the largest element
        if max_row_index != i: #if the row with the largest element in column i is not already row i, continue
            matrix[[i, max_row_index]] = matrix[[max_row_index, i]] #swapping the rows
    return matrix