import streamlit as st
import numpy as np
from functions.Shirley.Project_4.Cramers_rule import Cramers_rule
from global_functions_and_more.matrix_showcase import matrix_menu, display_matrix

def cramer_page_layout():
    st.title("Cramer's Rule")
    st.header("Theorem", divider="blue")
    st.write("Cramer’s rule expresses the solution of a system ${Ax=b}$ (where A is an n ${\\times}$ n matrix) of linear equations in terms of ratios of determinants")
    st.write("The unknown ${x_i}$ is equal to the ratio of the determinant created from the one of the matrix A by replacement of its ith column with a column of biases (“free” coefficients) to the determinant of the matrix A.")

    st.header("Calculation", divider="blue")
    st.subheader('Matrix Input')
    st.caption('Please enter the size of the augmented matrix.')
    col = st.columns(2)
    with col[0]:
        m = st.number_input('Number of rows (m)', min_value=1, value=2, key='m')
    with col[1]:
        n = st.number_input('Number of columns (n)', min_value=1, value=2, key='n')
    user_matrix = matrix_menu(m,n)
    display_matrix(user_matrix)
    pressed = st.button("Evaluate")
    if pressed:
        st.header("Results", divider="blue")
        matrix_a = np.array(user_matrix, dtype=float)
        # Validate dimensions
        if matrix_a.shape[1] != matrix_a.shape[0] + 1:
            st.error("The input must be an augmented matrix with one more column than rows.")
            return
        # Separate A and b matrices
        A = matrix_a[:, :-1]
        b = matrix_a[:, -1]
        # Check if determinant of A is zero
        if np.linalg.det(A) == 0:
            st.error("The determinant of matrix A is zero. The system has no unique solution.")
            return
            # Solve using Cramer's Rule
        results = Cramers_rule(matrix_a)
            # Display results
        st.write("Solution Vector")
        for i, val in enumerate(results):
            st.write(f"X[{i+1}] = {val:.4f}")
        else:
            "Sorry no solution"