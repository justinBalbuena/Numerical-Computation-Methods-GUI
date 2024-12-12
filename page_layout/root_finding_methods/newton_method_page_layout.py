import streamlit as st
from sympy import * #using this library for the derivative function
from global_functions_and_more.error_option import error_tolerance_methods
from global_functions_and_more.true_root import find_roots
from functions.Shirley.Project_3.Newtons_method import Newtons_Method

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
    newton_method_form = st.form(key="newton_method_form")
    error_method = newton_method_form.radio("Error tolerance method", error_tolerance_methods.keys())
    flag = error_tolerance_methods[error_method]()

    #the first in the form
    function = newton_method_form.text_input("Please enter a non-linear function")
    x0 = newton_method_form.text_input("Please enter x0:")
    tolerance = newton_method_form.number_input("Tolerance value (no negative)", value=None, format="%f",min_value=0.0000000000000000001)
    pressed = newton_method_form.form_submit_button("Evaluate")

    if pressed:
        # Results Section
        st.header("Results", divider="blue")
        root, count = Newtons_Method(x0, tolerance, flag, function)
        if root:
            st.write("Root Result: ", root, " Number of iterations: ", count)
        else:
            st.write("Root Not Found")