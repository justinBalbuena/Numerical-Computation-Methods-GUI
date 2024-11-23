import streamlit as st

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
    # Results Section
    st.header("Results", divider="blue")

