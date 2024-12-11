import streamlit as st

from functions.Ant.false_position_method import ant_FP_value_x1
from functions.Ant.secant_method import secant_method
from global_functions_and_more.convert_mathexpression import transform_math_expression
from global_functions_and_more.error_option import error_tolerance_methods
from global_functions_and_more.true_root import find_roots


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

    function = secant_form.text_input("Enter a function Ex. 2sin(x)-e^x/4-1")
    x0 = secant_form.number_input("Enter a number reasonable close to the root", value=None, format="%f")
    tolerance = secant_form.number_input("Enter tolerance", value=None, format="%f",
                                                 min_value=0.0000000000000000001)
    button = secant_form.form_submit_button("Evaluate")

    if button:
        # Results Section
        st.header("Results", divider="blue")
        function = transform_math_expression(function)
        true_root = find_roots(function, x0)
        x1 = ant_FP_value_x1(true_root,function)
        root = secant_method(x0,x1,tolerance,flag,function)
        st.write("The root found is: ",root)
        st.write("The true root is: ",true_root)

