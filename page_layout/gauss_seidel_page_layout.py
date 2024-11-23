import streamlit as st

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

    # Results Section
    st.header("Results", divider="blue")
