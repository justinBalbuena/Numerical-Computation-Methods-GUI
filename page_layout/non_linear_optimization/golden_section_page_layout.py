import streamlit as st

def golden_section_page_layout():
    # Golden Section Method
    st.title("Golden Section Method")

    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("Golden section method is one of the classical methods used in 1-D optimization")
    st.write("Like the bisection method for solving nonlinear equations, it has linear convergence, narrowing the bracketing interval in the golden proportion")

    # Calculation Section
    st.header("Inputs", divider="blue")
    a_value = st.text_input(label="**:blue[Left Bracket Value]**: ", key="a_value")
    b_value = st.text_input(label="**:blue[Right Bracket Value]**: ", key="b_value")
    tolerance = st.text_input(label="**:blue[Tolerance Value]**: ", key="tolerance_value")

    # Results Section
    st.header("Results", divider="blue")

