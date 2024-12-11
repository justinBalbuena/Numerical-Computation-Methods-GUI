import streamlit as st
import numpy as np
from functions.Ant.cramer_rule import ant_crammer_rule
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
        matrix_a = np.asmatrix(user_matrix)
        matrix_b = matrix_a[:,-1]
        matrix_a = np.delete(matrix_a,-1, 1)
        results = ant_crammer_rule(matrix_a,matrix_b)
        for i in range(len(results)):
            st.write(results[i])

