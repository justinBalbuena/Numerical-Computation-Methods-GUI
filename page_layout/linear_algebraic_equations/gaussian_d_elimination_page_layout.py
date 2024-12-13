import streamlit as st
import numpy as np
from global_functions_and_more.matrix_showcase import matrix_menu, display_matrix
from functions.Ant.linear_algebraic.gaussian_elim import gaussian_elimination


def gaussian_d_elimination_page_layout():
    st.title("Gaussian Elimination")
    st.header("Theorem", divider="blue")
    st.write("Extension of the method of trivial elimination to large sets of equations by developing a systematic algorithm to eliminate unknowns and to back substitute.")
    st.write("The Gaussian elimination method is based on subtracting the 1st equation from the ith equation to make the transformed coefficients in the first column equal to 0.")
    st.write("As a result, a matrix of the system becomes upper triangular.")

    st.header("Calculation", divider="blue")
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
        if n == m + 1:
            matrix_a = user_matrix
            results = gaussian_elimination(matrix_a)
            if results is not None:
                st.write("The result of the gaussian elimination method is:", results)
            else:
                st.write("The gaussian elimination method failed to converge!")
        else:
            st.write("it is an augmented matrix so column should be one more for the constants")