import numpy as np
def crammer_rule(matrix_a,matrix_b):
    array_solution = []
    det = round(np.linalg.det(matrix_a))
    if det == 0:
        print("The determinant is 0!")
        exit()
    temp_array = matrix_a.copy()
    for i in range(len(matrix_a)):
        temp_array[:,i] = matrix_b[:,0]
        temp_det = round(np.linalg.det(temp_array))
        array_solution.append(temp_det/det)
        temp_array = matrix_a.copy()
    return array_solution
print("For Augmented Matrix")
num_of_row = int(input("how many rows does you matrix have?: "))
num_of_col = int(input("how many columns does you matrix have?: "))
print("Enter Matrix (uses spaces, Augmented): ")
numbers = list(map(float,input().split()))
matrix_a = np.matrix(numbers).reshape(num_of_row, num_of_col)
matrix_b = matrix_a[:,num_of_col-1]
matrix_a = np.delete(matrix_a,num_of_col-1,1)
answer = crammer_rule(matrix_a,matrix_b)
print("Solution set is: ",answer)