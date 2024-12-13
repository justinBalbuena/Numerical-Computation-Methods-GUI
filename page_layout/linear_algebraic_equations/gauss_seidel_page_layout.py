import streamlit as st
import numpy as np
from global_functions_and_more.error_option import error_tolerance_methods_iter
from global_functions_and_more.matrix_showcase import matrix_menu, display_matrix
from functions.Shirley.Project_6.Gauss_Seidel import diag_dominant, transform_dd, gauss_seidel

# Gauss-Seidel Iterative Method Layout
def gauss_seidel_page_layout():
    """
    Streamlit UI for Gauss-Seidel Iterative Method.
    """
    st.title("Gauss-Seidel Iterative Method")

    # Theorem section
    st.header("Theorem", divider="blue")
    st.write(
        "The Gauss-Seidel method usually converges faster than the Jacobi method. "
        "It is important to ensure that the matrix is diagonally dominant for convergence. "
        "This method updates each variable sequentially based on the latest available values."
    )

    # Inputs for error tolerance method
    st.header("Calculation Inputs", divider="blue")
    error_method = st.radio("Error tolerance method", error_tolerance_methods_iter.keys())
    flag = error_tolerance_methods_iter[error_method]()
    tolerance = st.number_input("Enter the tolerance value", value=0.001, format="%f", min_value=1e-15)

    # Input for augmented matrix dimensions
    st.header("Input Augmented Matrix", divider="blue")
    col = st.columns(2)
    with col[0]:
        m = st.number_input('Number of rows (m):', min_value=1, value=2, key='m')  # Number of equations
    with col[1]:
        n = st.number_input('Number of columns (n):', min_value=2, value=3, key='n')  # Coefficients + augmented column

    user_matrix = matrix_menu(m, n)
    display_matrix(user_matrix)

    # Button to evaluate Gauss-Seidel method
    pressed = st.button("Evaluate")
    if pressed:
        try:
            # Validate input matrix dimensions
            if user_matrix.shape != (m, n):
                st.error("The dimensions of the input matrix do not match the specified rows and columns.")
                return

            # Extract coefficient matrix (A) and augmented column (b)
            A_matrix = user_matrix[:, :-1]
            b = user_matrix[:, -1]

            # Check diagonal dominance
            if not diag_dominant(A_matrix):
                st.warning("Matrix is not diagonally dominant. Attempting transformation...")
                user_matrix = transform_dd(user_matrix)
                A_matrix = user_matrix[:, :-1]
                b = user_matrix[:, -1]
                st.write("Transformed Augmented Matrix:")
                display_matrix(user_matrix)

            # Initial guess for solution
            x_initial = np.ones(A_matrix.shape[0])

            # Perform Gauss-Seidel iteration
            solution = gauss_seidel(A_matrix, b, x_initial, flag, tolerance)

            # Display solution
            st.success("Gauss-Seidel Method Converged Successfully!")
            st.write("Solution Vector:")
            st.write(solution)
        except Exception as e:
            st.error(f"An error occurred: {e}")