import numpy as np

def compute_error(new_x, old_x, stop_c): #creating a function for the MAE and RMSE
    if stop_c == '1': #if the user chose 1, do the MAE
        return np.mean(np.abs(new_x - old_x)) #calculating the mean absolute error
    elif stop_c == '2':  #if the user chose 2, do the MAE
        return np.sqrt(np.mean((new_x - old_x)**2)) #calculating the approximate root mean square error
    else:
        raise ValueError("Please choose 1 or 2.") #error message if the user chose anything else

def gauss_seidel(A_matrix, tolerance, stop_c): #creating the gauss-seidel function
    A = A_matrix[:, :-1] #everything excluding the augmented part of the matrix
    b = A_matrix[:, -1] #augmented part of the matrix
    n = len(b) #setting n equal to the length of augmented part of the matrix
    x = np.ones(n) #starting points
    old_x = np.copy(x) #storing old x for calculation
    error = float(10) #initializing error
    while error > tolerance: #if error is less than the tolerance, continue
        for i in range(n): #going through the rows
            x[i] = b[i] #setting values of x equal to b value
            for j in range(n): #going through the rows
                if i != j: #if i does not equal j, continue
                    x[i] -= A[i, j] * x[j] #subtract x(i) by A(i, j) times x(j)
            x[i] /= A[i, i]  #setting x(i) equal to diagonal value
        error_value = compute_error(x, old_x, stop_c) #calling the function to let the user choose which method, RMSE or MAE
        if error_value < tolerance: #if the error value is less than the tolerance, break
            break
        old_x = x.copy() #changing old x to be equal to x
    return x

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

#main
A_matrix = np.array([[3, 1, -4, 7], [-2, 3, 1, -5], [2, 0, 5, 10]],float)
#creating my first matrix
B_matrix = np.array([[1, -2, 4, 6], [8, -3, 2, 2], [-1, 10, 2, 4]],float)
#creating my second matrix
print("The first matrix we're working with is: \n", A_matrix) #printing the first and second matrix
print("\nThe second matrix we're working with is: \n", B_matrix) #printing the first and second matrix
#asking for the user for the tolerance
print("Please enter the tolerance:")
tolerance = float(input("Ex: 0.001: "))
#asking for the stopping criteria
stop_c = input("Please enter 1 for MAE or 2 for RMSE: ")
#checking to see if matrix is not diagonally dominant
if not diag_dominant(A_matrix[:, :-1]): #if it is, then call the tranform_dd function
    A_matrix = transform_dd(A_matrix)
    B_matrix = transform_dd(B_matrix)

#printing the output from both functions
x_gs = gauss_seidel(A_matrix, tolerance, stop_c)
x_gs2 = gauss_seidel(B_matrix, tolerance, stop_c)

#displaying the solutions
print("Gauss-Seidel solution:", '\nFirst Matrix: ' , x_gs)
print("\nSecond Matrix: ", x_gs2)