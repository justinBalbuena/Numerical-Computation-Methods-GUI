import streamlit as st

def composite_simpson_page_layout():
    # Composite Simpson's Rule
    st.title("Composite Simpson's Rule")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("More accurate estimate of an integral is obtained if a higher-order polynomial is used to connect the points. The formulas that result from taking the integrals under such polynomials are called Simpson’s rules")
    st.write("Divide the interval into n sub-intervals and apply Simpson’s Rule on each consecutive pair of sub-intervals. Note that n must be even")
    # Calculation Section
    st.header("Calculation", divider="blue")

    # Results Section
    st.header("Results", divider="blue")
