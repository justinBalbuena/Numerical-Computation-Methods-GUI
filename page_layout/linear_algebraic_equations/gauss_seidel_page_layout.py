import streamlit as st
from global_functions_and_more.error_option import error_tolerance_methods_iter
from global_functions_and_more.matrix_showcase import matrix_menu,display_matrix
import numpy as np
from sympy import *
from functions.justin.project6.gauss_seidal import gauss_seidel

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

        st.header("Results", divider="blue")

        matrix_a = Matrix(user_matrix)

        results = gauss_seidel(matrix_a, tolerance, flag)
        if results is not None:
            for i in range(len(results)):
                st.write(float(results[i]))
        else:
             st.write("There was no unique solution")
