import streamlit as st
import numpy as np

from functions.Ant.jacobi_method import ant_jacobi
from global_functions_and_more.matrix_showcase import matrix_menu, display_matrix
from global_functions_and_more.error_option import error_tolerance_methods_iter


def jacobi_method_page_layout():
    # Jacobi Iterative Method
    st.title("Jacobi Iterative Method")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("It is important to take into account that if a matrix of the system is not diagonally dominant, an iterative method may not converge!")
    st.write("Hence it is very important to start any iterative algorithm from making a matrix of a system diagonally dominant!")
    st.write("In the Jacobi method, the ith iteration consists of finding a new approximation based on the previous approximation")

    # Calculation Section
    st.header("Calculation", divider="blue")
    error_method = st.radio("Error tolerance method",error_tolerance_methods_iter.keys())
    flag = error_tolerance_methods_iter[error_method]()
    tolerance = st.number_input("Enter the tolerance value",value=.0001,format="%f",min_value=0.0000000000000000001)
    st.header("Input Augmented Matrix")
    col = st.columns(2)
    with col[0]:
        m = st.number_input('Number of rows (m)', min_value=1, value=2, key='m')
    with col[1]:
        n = st.number_input('Number of columns (n)', min_value=1, value=2, key='n')
    user_matrix = matrix_menu(m, n)
    display_matrix(user_matrix)
    pressed = st.button("Evaluate")
    if pressed and n == m+1:
        matrix_a = user_matrix
        matrix_b = user_matrix[:,-1]
        matrix_a = np.delete(matrix_a, -1, 1)
        initial_guess = np.zeros(n-1, dtype=float)
        results =  ant_jacobi(matrix_a, matrix_b, initial_guess,flag,tolerance)
        if results is not None:
             st.write("The result of the Jacobi method is:", results)
        else:
             st.write("The Jacobi method failed to converge!")
    else:
        st.write("it is an augmented matrix so column should be one more for the constants")
