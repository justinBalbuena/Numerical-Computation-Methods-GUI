import streamlit as st

def secant_page_layout():
    # Secant Method
    st.title("Secant Method")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("Requires two initial estimates of x: x0 , x1. However, because f(x) is not required to change signs between estimates, it is not classified as a bracketing method")
    st.write("Convergence is not guaranteed for arbitrary chosen x0")
    # Calculation Section
    st.header("Calculation", divider="blue")
    # Results Section
    st.header("Results", divider="blue")
