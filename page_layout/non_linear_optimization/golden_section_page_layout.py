import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sympy import lambdify, symbols, Symbol

from global_functions_and_more.convert_mathexpression import transform_math_expression
from global_functions_and_more.error_option import extrema_types
from functions.Ant.non_linear_optimize.golden_section import golden_section_method

def golden_section_page_layout():
    # Golden Section Method
    st.title("Golden Section Method")

    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("Golden section method is one of the classical methods used in 1-D optimization")
    st.write("Like the bisection method for solving nonlinear equations, it has linear convergence, narrowing the bracketing interval in the golden proportion")

    # Calculation Section
    st.header("Inputs", divider="blue")
    golden_section_form = st.form(key="golden_section_form")
    function = golden_section_form.text_input("Enter a function Ex. 2sin(x)-e^x/4-1")
    extrema_type = golden_section_form.radio("Extrema Kind: ", extrema_types.keys())
    flag = extrema_types[extrema_type]()
    left_bracket = golden_section_form.number_input(label="Enter a value for the left bracket", value=None, format="%f")
    right_bracket = golden_section_form.number_input(label="Enter a value for the right bracket", value=None, format="%f")
    tolerance = golden_section_form.number_input(label="Enter a tolerance value", value=None, format="%f")

    pressed = golden_section_form.form_submit_button("Evaluate")

    if pressed:
        # Results Section
        st.header("Results", divider="blue")

        function = transform_math_expression(function)
        results = golden_section_method(left_bracket, right_bracket, function, tolerance,flag)
        st.write(f"The x value of the local extrema is: **:blue[{results[0]}]**")
        user_function = lambdify(Symbol('x'), function)
        f_x = float(user_function(results[0]))
        st.write(f"The y value of the local extrema is: **:blue[{f_x}]**")

        #Graph Implementation
        fig, ax = plt.subplots()

        #generating x-values for plotting
        x = Symbol('x')
        user_function = lambdify(x, function)
        x_values = np.linspace(left_bracket, right_bracket, 500)
        y_values = [user_function(x) for x in x_values]

        #plotting the function
        ax.plot(x_values, y_values, color='blue', label='Function')
        #plotting the extrema
        ax.scatter(results[0], f_x, color='red', label="Extrema")
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        ax.set_xlabel('X values')
        ax.set_ylabel('Y values')
        ax.set_title('Local Extrema:')
        ax.legend()
        st.pyplot(fig)