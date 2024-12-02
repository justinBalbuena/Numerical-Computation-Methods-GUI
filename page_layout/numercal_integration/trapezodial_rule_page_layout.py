import streamlit as st


def trapezoidal_rule_page_layout():
    # Multiple Application of Trapezoidal Rule
    st.title("Multiple Application of Trapezoidal Rule")

    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("One way to improve the accuracy of the trapezoidal rule is to divide the integration interval from a to b into a number of equal segments of the length h and apply the method to each segment")
    st.write("The areas of individual segments can then be added to yield the integral for the entire interval")

    # Calculation Section
    st.header("Calculation", divider="blue")

    # Results Section
    st.header("Results", divider="blue")