import numpy as np
def ant_crammer_rule(matrix_a,matrix_b):
    array_solution = []
    det = round(np.linalg.det(matrix_a))
    if det == 0:
        return 0
    temp_array = matrix_a.copy()
    for i in range(len(matrix_a)):
        temp_array[:,i] = matrix_b[:,0]
        temp_det = round(np.linalg.det(temp_array))
        array_solution.append(temp_det/det)
        temp_array = matrix_a.copy()
    return array_solution
