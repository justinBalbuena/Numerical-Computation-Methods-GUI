import numpy as np
import streamlit as st
from global_functions_and_more.convert_mathexpression import transform_math_expression
from functions.justin.project10.newtons_for_extrema import newtons_for_extrema
import matplotlib.pyplot as plt
from sympy import *

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
        results = newtons_for_extrema(x0_val, tolerance, function)
        st.write(f"The x value of the local extrema is: **:blue[{results[0]}]**")
        st.write(f"The y value of the local extrema is: **:blue[{results[1]}]**")
        st.write(f"The amount of iterations it took was: **:blue[{results[2]}]**")
        #Graph Implementation
        fig, ax = plt.subplots()

        #generating x-values for plotting
        x = Symbol('x')
        user_function = lambdify(x, function)
        x_values = newtons_for_extrema(x0_val,tolerance,function)

        function = function.replace('E', '2.718281828459045')
        user_function = lambdify(x, function)
        leftx = min(x_values)-2
        rightx = max(x_values)+2
        x_values = np.linspace(leftx,rightx,500)
        y_values = [user_function(x) for x in x_values]


        #plotting the function
        ax.plot(x_values, y_values, color='blue', label='Function')
        #plotting the extrema
        ax.scatter(results[0], results[1], color='red', label="Extrema")
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        ax.set_xlabel('X values')
        ax.set_ylabel('Y values')
        ax.set_title('Local Extrema:')
        ax.legend()
        st.pyplot(fig)