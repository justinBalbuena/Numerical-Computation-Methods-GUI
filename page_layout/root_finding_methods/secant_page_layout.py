import streamlit as st
from sympy import *

from functions.Shirley.Project_2.Secant_and_false_position import secant_method
from global_functions_and_more.convert_mathexpression import transform_math_expression
from global_functions_and_more.error_option import error_tolerance_methods
from global_functions_and_more.true_root import find_roots, find_roots_sympy


def secant_page_layout():
    # Secant Method
    st.title("Secant Method")

    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("Requires two initial estimates of x: x0 , x1. However, because f(x) is not required to change signs between estimates, it is not classified as a bracketing method")
    st.write("Convergence is not guaranteed for arbitrary chosen x0")

    # Calculation Section
    st.header("Calculation", divider="blue")
    secant_form = st.form(key="false_position_form")
    error_method = secant_form.radio("Error Tolerance Method", error_tolerance_methods.keys())
    flag = error_tolerance_methods[error_method]()

    function = secant_form.text_input("Please enter a function Ex. 4*sin(x)-(sqrt(x))+log(2*x)")
    x0 = secant_form.number_input("Please enter x0", value=None, format="%f")
    x1 = secant_form.number_input("Please enter x1", value=None, format="%f")
    tolerance = secant_form.number_input("Enter the tolerance", value=None, format="%f",
                                                 min_value=0.0000000000000000001)
    button = secant_form.form_submit_button("Evaluate")

    if button:
        # Results Section
        st.header("Results", divider="blue")
        # function = transform_math_expression(function)
        # true_root = find_roots(function, x0)
        # x1 = ant_FP_value_x1(true_root,function)
        # function = transform_math_expression(function)
        x = symbols('x')
        function_sympy = transform_math_expression(function)
        function_norm = transform_math_expression(function)
        root,count = secant_method(x0,x1,tolerance,flag,function_sympy)
        if root:
             st.write("The Root of the function is: ", root)
             st.write("The amount of iterations taken is: ", count)
             true_root = find_roots_sympy(function_sympy,x0)
             st.write("True Value: ", true_root)
        else:
            st.write("The root could not be found!")