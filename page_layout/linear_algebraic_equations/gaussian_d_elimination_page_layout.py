import streamlit as st
from sympy import Matrix
from functions.Shirley.Project_5.Gaussian_elimation import gaussian

def gaussian_d_elimination_page_layout():
    st.title("Gaussian Elimination")
    st.header("Theorem", divider="blue")
    st.write("Extension of the method of trivial elimination to large sets of equations by developing a systematic algorithm to eliminate unknowns and to back substitute.")
    st.write("The Gaussian elimination method is based on subtracting the 1st equation from the ith equation to make the transformed coefficients in the first column equal to 0.")
    st.write("As a result, a matrix of the system becomes upper triangular.")
    st.header("Calculation", divider="blue")

    # Input the size of the matrix
    matrix_size = st.number_input("Enter the size of the square matrix (e.g., 2, 3, 4):", min_value=2, step=1)

    if matrix_size:
        matrix_size = int(matrix_size)

        st.write("Enter the coefficients of the matrix:")
        user_matrix = []
        for i in range(matrix_size):
            row = st.text_input(f"Row {i+1} (comma-separated):", key=f"row_{i}")
            if row:
                user_matrix.append([float(x) for x in row.split(",")])

        st.write("Enter the constants (comma-separated):")
        constants_input = st.text_input("Constants:", key="constants")

        if st.button("Calculate Solution"):
            if len(user_matrix) == matrix_size and constants_input:
                try:
                    constants = [float(x) for x in constants_input.split(",")]
                    matrix = Matrix(user_matrix)
                    constants_col = Matrix(constants)

                    augmented_matrix = matrix.col_insert(matrix_size, constants_col)
                    solution = gaussian(augmented_matrix)

                    st.header("Results")
                    if solution:
                        st.write("Solution:", solution)
                    else:
                        st.error("No unique solution found.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.error("Please provide valid inputs for all rows and constants.")
