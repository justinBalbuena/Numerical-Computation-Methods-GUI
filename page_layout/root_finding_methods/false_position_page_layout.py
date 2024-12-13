import streamlit as st

from global_functions_and_more.true_root import find_roots
from global_functions_and_more.convert_mathexpression import transform_math_expression
from global_functions_and_more.error_option import error_tolerance_methods
from functions.justin.project2.falsePosition import false_position

def false_position_page_layout():
    # False Position Method
    st.title("False Position Method")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("The method of false position takes care of bracketing a root using x0, x1 chosen such that f(x0), f(x1) are of opposite sign (in the same way as for the bisection method)")
    st.write("Unlike the bisection method, this method determines its step not by taking the midpoint between the two x-values, but by taking the intersection point of a line connecting the brackets x0, x1 and the x-axis")

    # Calculation Section
    st.header("Calculation", divider="blue")
    false_position_form = st.form(key="false_position_form")
    error_method = false_position_form.radio("Error Tolerance Method",error_tolerance_methods.keys())
    flag = error_tolerance_methods[error_method]()

    function = false_position_form.text_input("Enter a function Ex. 2sin(x)-e^x/4-1")
    x0 = false_position_form.number_input("Enter x0",value=None,format="%f")
    x1 = false_position_form.number_input("Enter x1", value=None, format="%f")
    tolerance = false_position_form.number_input("Enter tolerance",value=None,format="%f",min_value=0.0000000000000000001)
    button = false_position_form.form_submit_button("Evaluate")

    if button:
        # Results Section
        st.header("Results", divider="blue")
        function = transform_math_expression(function)

        root = false_position(x0, x1, flag, function, tolerance)
        if root:
             st.write("The Root of the function is: ", root[0])
             st.write("The amount of iterations taken is: ", root[1])
             true_root = find_roots(function,x0)
             st.write("True Value: ", true_root)
        else:
            st.write("The root could not be found!")