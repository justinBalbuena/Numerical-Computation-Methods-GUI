import streamlit as st

def newton_method_page_layout():
    # Newton's Method
    st.title("Newton's Method")
    st.write("Idea is most nonlinear functions can be approximated by a set of tangents over small intervals")
    st.write("A convenient method for functions whose derivatives can be evaluated analytically. It may not be convenient for functions whose derivatives cannot be evaluated analytically.")
    st.write("may not converge on some occasions")
    # Theorem section
    st.header("Theorem", divider="blue")

    # Calculation Section
    st.header("Calculation", divider="blue")

    # Results Section
    st.header("Results", divider="blue")
