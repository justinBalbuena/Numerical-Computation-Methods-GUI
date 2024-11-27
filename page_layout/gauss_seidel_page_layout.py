import streamlit as st
from global_functions_and_more.error_option_iterative import error_tolerance_methods_iter
from global_functions_and_more.matrix_showcase import matrix_menu,display_matrix
import numpy as np
from functions.Ant.gauss_seidel_method import ant_seidel

def gauss_seidel_page_layout():
    # Gauss-Seidel Iterative Method
    st.title("Gauss-Seidel Iterative Method")

    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("The Gauss-Seidel method usually converges faster than the Jacobi method")
    st.write("It is important to take into account that if a matrix of the system is not diagonally dominant, an iterative method may not converge!")
    st.write("Hence it is very important to start any iterative algorithm from making a matrix of a system diagonally dominant!")
    st.write("In the Gauss-Seidel method, the ith iteration consists of finding a new approximation based on the latest currently available values")

    # Calculation Section
    st.header("Calculation", divider="blue")
    error_method = st.radio("Error tolerance method",error_tolerance_methods_iter.keys())
    flag = error_tolerance_methods_iter[error_method]()
    tolerance = st.number_input("Enter the tolerance value",value=None,format="%f",min_value=0.0000000000000000001)
    st.header("Input Augmented Matrix")
    col = st.columns(2)
    with col[0]:
        m = st.number_input('Number of rows (m)', min_value=1, value=2, key='m')
    with col[1]:
        n = st.number_input('Number of columns (n)', min_value=1, value=2, key='n')
    user_matrix = matrix_menu(m, n)
    display_matrix(user_matrix)
    pressed = st.button("Evaluate")
    if pressed:
        matrix_a = user_matrix
        matrix_b = user_matrix[:,-1]
        matrix_a = np.delete(matrix_a, -1, 1)
        initial_guess = np.zeros(n-1, dtype=float)
        results =  ant_seidel(matrix_a, matrix_b, initial_guess,flag,tolerance)
        if results:
             st.write("The result of the Jacobi method is:", results)
        else:
             st.write("The Jacobi method failed to converge!")
