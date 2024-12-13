import numpy as np
import streamlit as st
from global_functions_and_more.convert_mathexpression import transform_math_expression
from global_functions_and_more.error_option import extrema_types
from functions.Ant.non_linear_optimize.newton_method import newton_method_min_max
import matplotlib.pyplot as plt
from sympy import lambdify, symbols, Symbol

def newton_op_page_layout():
    # Newton’s Method for Optimization
    st.title("Newton’s Method for Optimization")

    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("The Newton’s method is based on approaching a min (max) of a continuous nonlinear function f starting from some x0 selected in a reasonable proximity from the expected solution and using an iterative process where each step is proportional to the ratio of the 1st and 2nd derivatives")

    # Calculation
    st.header("Inputs", divider="blue")
    newtons_form = st.form(key="newtons_method_form")
    function = newtons_form.text_input("Enter a function Ex. 2sin(x)-e^x/4-1")
    x0_val = newtons_form.number_input(label="Enter a starting point value", value=None, format="%f")
    tolerance = newtons_form.number_input(label="Enter a tolerance value", value=None, format="%f")

    pressed = newtons_form.form_submit_button("Evaluate")

    if pressed:
        # Results Section
        st.header("Results", divider="blue")

        function = transform_math_expression(function)
        results = newton_method_min_max(x0_val, function, tolerance)
        st.write(f"The x value of the local extrema is: **:blue[{results[0]}]**")
        user_function = lambdify(symbols("x"), function)
        f_x = user_function(results[0])
        st.write(f"The y value of the local extrema is: **:blue[{f_x}]**")

        #Graph Implementation
        fig, ax = plt.subplots()

        #generating x-values for plotting
        x = Symbol('x')
        user_function = lambdify(x, function)
        x_values = newton_method_min_max(x0_val,function,tolerance)
        leftx = min(x_values)-2
        rightx = max(x_values)+2
        x_values = np.linspace(leftx,rightx,500)
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