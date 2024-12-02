import streamlit as st
def gaussian_d_elimination_page_layout():
    # Gaussian Directed Elimination
    st.title("Gaussian Elimination")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("Extension of the method of trivial elimination to large sets of equations by developing a systematic algorithm to eliminate unknowns and to back substitute")
    st.write("The Gaussian elimination method is based on subtracting the 1st equation from the ith equation to make the transformed coefficients in the first column equal to 0")
    st.write("As a result, a matrix of the system becomes upper triangular")

    # Calculation Section
    st.header("Calculation", divider="blue")

    # Results Section
    st.header("Results", divider="blue")
