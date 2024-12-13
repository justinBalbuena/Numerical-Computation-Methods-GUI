import streamlit as st

from global_functions_and_more.convert_mathexpression import transform_math_expression
from global_functions_and_more.error_option import error_tolerance_methods
from functions.justin.project3.newtons import newtons

def newton_method_page_layout():
    # Newton's Method
    st.title("Newton's Method")
    st.write("Idea is most nonlinear functions can be approximated by a set of tangents over small intervals")
    st.write("A convenient method for functions whose derivatives can be evaluated analytically. It may not be convenient for functions whose derivatives cannot be evaluated analytically.")
    st.write("may not converge on some occasions")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("If f(x) is a real, continuously differentiable function and f'(x) != 0 at the initial guess x0, then Newton's Method converges to a root of f(x) = 0 near x0 provided x0 is sufficiently close to the actual root.")

    # Calculation Section
    st.header("Calculation", divider="blue")
    newton_method_form = st.form(key="newton_method_form")
    error_method = newton_method_form.radio("Error tolerance method", error_tolerance_methods.keys())
    flag = error_tolerance_methods[error_method]()

    #the first in the form
    function = newton_method_form.text_input("Please enter a non-linear function")
    function = transform_math_expression(function)
    x_guess = newton_method_form.number_input("Please enter an initial guess for x",value=None)
    tolerance = newton_method_form.number_input("Tolerance value (no negative)", value=None, format="%f",min_value=0.0000000000000000001)
    pressed = newton_method_form.form_submit_button("Evaluate")

    if pressed:
         root,iterations = newtons(x_guess, flag, function, tolerance)
         if root:
            st.write("Root Result: ", root, " Number of iterations: ", iterations)
         else:
            st.write("Root Not Found")
