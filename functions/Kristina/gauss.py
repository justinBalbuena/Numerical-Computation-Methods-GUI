import streamlit as st
from sympy import Matrix

# Function for Gaussian elimination with pivoting
def gauss_with_pivot(a):
    """
    :param a: the augmented matrix
    :return: the list of solutions or error message
    """
    row_indices = a.shape[0]

    # Forward elimination
    for i in range(row_indices - 1):
        pivot = i
        for j in range(i + 1, row_indices):
            if abs(a[j, i]) > abs(a[i, i]):
                pivot = j

        if pivot != i:
            a.row_swap(i, pivot)

        if a[i, i] == 0:
            return "No unique solution"

        for j in range(i + 1, row_indices):
            multiplier = a[j, i] / a[i, i]
            for k in range(i + 1, row_indices + 1):
                a[j, k] = a[j, k] - (multiplier * a[i, k])

    if a[row_indices - 1, row_indices - 1] == 0:
        return "No unique solution"

    x = [0] * row_indices

    # Back substitution
    x[row_indices - 1] = a[row_indices - 1, row_indices] / a[row_indices - 1, row_indices - 1]
    for i in range(row_indices - 2, -1, -1):
        accumulation = 0
        for j in range(i + 1, row_indices):
            accumulation += a[i, j] * x[j]
        x[i] = ((a[i, row_indices] - accumulation) / a[i, i])

    return x