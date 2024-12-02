import streamlit as st

def golden_section_page_layout():
    # Golden Section Method
    st.title("Golden Section Method")

    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("Golden section method is one of the classical methods used in 1-D optimization")
    st.write("Like the bisection method for solving nonlinear equations, it has linear convergence, narrowing the bracketing interval in the golden proportion")

    # Calculation Section
    st.header("Calculation", divider="blue")
    points = st.number_input("Number of data points",value=None,min_value=2)
    # Results Section
    st.header("Results", divider="blue")

