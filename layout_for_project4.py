
from functions.Newton_Method import newton
import streamlit as st

def absolute_error_method():
    return "a"
def relative_error_method():
    return "b"
def true_absolute_error_method():
    return "c"
def combination():
    return "d"
def run_page_4():
    error_tolerance_methods = {
        "Absolute Error": absolute_error_method,
        "Relative Error": relative_error_method,
        "True Absolute Error": true_absolute_error_method,
        "Combination of Absolute Error and Relative Error": combination
    }
    st.title("Newton Method for solving non-linear")
    newton_method_form = st.form(key="newton_method_form")
    error_method = newton_method_form.radio("Error tolerance method", error_tolerance_methods.keys())
    flag = error_tolerance_methods[error_method]()

    #the first in the form
    function = newton_method_form.text_input("Please enter a non-linear function")
    x_guess = newton_method_form.number_input("Please enter an initial guess for x")
    tolerance = newton_method_form.number_input("Tolerance value (no negative)", value=None, format="%f",min_value=0.0000000000000000001)
    pressed = newton_method_form.form_submit_button("Evaluate")

    if pressed:
         root,iterations = newton(x_guess, function, tolerance,flag)
         if root:
            st.write("Root Result: ", root, " Number of iterations: ", iterations)
         else:
            st.write("Root Not Found")