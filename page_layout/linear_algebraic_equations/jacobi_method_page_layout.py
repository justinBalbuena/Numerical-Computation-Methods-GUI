import streamlit as st
import numpy as np

#from functions.Ant.jacobi_method import ant_jacobi
from global_functions_and_more.matrix_showcase import matrix_menu, display_matrix
from global_functions_and_more.error_option import error_tolerance_methods_iter
from functions.Shirley.Project_6 import Jacobi
from functions.Shirley.Project_6.Jacobi import jacobi

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
    stop_c = error_tolerance_methods_iter[error_method]()
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
        A_matrix = user_matrix
        #initial_guess = np.zeros(n-1, dtype=float)
        new_x = np.zeros(n)  # creating a matrix of zeros to be updated
        old_x = new_x.copy() #creating a copy of old_x
        results =  jacobi(A_matrix, tolerance, stop_c)
        if results is not None:
             st.write("The result of the Jacobi method is:", results)
        else:
             st.write("The Jacobi method failed to converge!")

