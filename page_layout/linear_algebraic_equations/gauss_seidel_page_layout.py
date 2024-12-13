import streamlit as st
import numpy as np
from global_functions_and_more.error_option import error_tolerance_methods_iter
from global_functions_and_more.matrix_showcase import matrix_menu, display_matrix
from functions.Shirley.Project_6.Gauss_Seidel import gauss_seidel, diag_dominant, transform_dd

def gauss_seidel_page_layout():
    # Gauss-Seidel Iterative Method
    st.title("Gauss-Seidel Iterative Method")

    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("The Gauss-Seidel method usually converges faster than the Jacobi method.")
    st.write("It is important to ensure that the matrix is diagonally dominant for convergence.")
    st.write("This method updates each variable sequentially based on the latest available values.")

    # Calculation Section
    st.header("Calculation", divider="blue")
    error_method = st.radio("Error tolerance method", error_tolerance_methods_iter.keys())  # User chooses error metric
    flag = error_tolerance_methods_iter[error_method]()
    tolerance = st.number_input("Enter the tolerance value", value=0.001, format="%f", min_value=1e-15)

    st.header("Input Augmented Matrix")
    col = st.columns(2)
    with col[0]:
        m = st.number_input('Number of rows (m)', min_value=1, value=2, key='m')  # Number of equations
    with col[1]:
        n = st.number_input('Number of columns (n)', min_value=2, value=3, key='n')  # Coefficients + Augmented column

    user_matrix = matrix_menu(m, n)
    display_matrix(user_matrix)

    pressed = st.button("Evaluate")
    if pressed:
        try:
            # Validate input matrix dimensions
            if user_matrix.shape != (m, n):
                st.error("The dimensions of the input matrix do not match the specified rows and columns.")
                return

            # Extract A (coefficients) and b (augmented column)
            if user_matrix.shape[1] < 2:
                st.error("Input matrix must have at least 2 columns (coefficients and augmented column).")
                return
            A_matrix = user_matrix[:, :-1]  # Coefficients of the system
            b = user_matrix[:, -1]  # Constants (augmented column)

            # Ensure matrix is diagonally dominant
            if not diag_dominant(A_matrix):
                st.warning("Matrix is not diagonally dominant. Transforming matrix...")
                user_matrix = transform_dd(user_matrix)
                A_matrix = user_matrix[:, :-1]  # Update coefficients after transformation
                b = user_matrix[:, -1]  # Update constants after transformation
                st.write("Transformed Augmented Matrix:")
                display_matrix(user_matrix)
            # Initial guess
            x = np.ones(A_matrix.shape[0])
            # Perform Gauss-Seidel method
            results = gauss_seidel(A_matrix, b, x, flag, tolerance)
            st.success("Gauss-Seidel Method Converged!")
            st.write("Solution Vector:")
            st.write(results)
        except Exception as e:
            st.error(f"An error occurred: {e}")
