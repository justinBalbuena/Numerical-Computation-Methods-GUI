import streamlit as st

def gauss_jordan_d_elimination_page_layout():
    # Gauss-Jordan Directed Elimination
    st.title("Gauss-Jordan Directed Elimination")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("It is a variation of Gaussian elimination.")
    st.write("The idea is that the elements above the diagonal are made zero while zeros are created also below the diagonal.")
    st.write("Elimination step results in the identity matrix.")
    st.write("Consequently, it is not necessary to employ back substitution to obtain solution because the solution is resulted from the elimination procedure.")
    # Calculation Section
    st.header("Calculation", divider="blue")

    # Results Section
    st.header("Results", divider="blue")