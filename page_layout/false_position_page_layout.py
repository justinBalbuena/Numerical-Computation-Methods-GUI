import streamlit as st
def false_position_page_layout():
    # False Position Method
    st.title("False Position Method")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("The method of false position takes care of bracketing a root using x0, x1 chosen such that f(x0), f(x1) are of opposite sign (in the same way as for the bisection method)")
    st.write("Unlike the bisection method, this method determines its step not by taking the midpoint between the two x-values, but by taking the intersection point of a line connecting the brackets x0, x1 and the x-axis")
    # Calculation Section
    st.header("Calculation", divider="blue")


    # Results Section
    st.header("Results", divider="blue")
