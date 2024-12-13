import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sympy import lambdify, symbols, Symbol

from global_functions_and_more.convert_mathexpression import transform_math_expression
from global_functions_and_more.error_option import extrema_types
from functions.justin.project10.newtons_for_extrema import newtons_for_extrema


def newton_op_page_layout():
    """
    Newton’s Method for Optimization Streamlit Layout
    """
    # Title
    st.title("Newton’s Method for Optimization")

    # Theorem explanation
    st.header("Theorem", divider="blue")
    st.write(
        "Newton’s method is based on approaching a minimum (or maximum) of a continuous nonlinear function `f` "
        "starting from an initial point `x₀`. The method uses an iterative process where each step is proportional to "
        "the ratio of the 1st and 2nd derivatives of the function."
    )

    # Inputs section
    st.header("Inputs", divider="blue")
    newtons_form = st.form(key="newtons_method_form")
    function_input = newtons_form.text_input("Enter a function (e.g., 2*sin(x)-exp(x)/4-1):")
    x0_val = newtons_form.number_input("Enter the starting point (x₀):", value=0.0, format="%f")
    tolerance = newtons_form.number_input("Enter the tolerance value:", value=0.001, format="%f")

    pressed = newtons_form.form_submit_button("Evaluate")

    if pressed:
        # Transform the input function into a callable form
        x = Symbol('x')  # Symbol for lambdification
        symbolic_function = transform_math_expression(function_input)
        f = lambdify(x, symbolic_function)

        # Run Newton's method for extrema
        results = newtons_for_extrema(x0_val, tolerance, symbolic_function)

        # Display results
        st.header("Results", divider="blue")
        st.write(f"The x value of the local extrema is: **:blue[{results[0]:.4f}]**")
        st.write(f"The y value of the local extrema is: **:blue[{results[1]:.4f}]**")
        st.write(f"The number of iterations: **:blue[{results[2]}]**")

        # Graph Implementation
        st.subheader("Function Plot")
        x_values = np.linspace(results[0] - 2, results[0] + 2, 500)  # Focused range near extrema
        y_values = [f(val) for val in x_values]

        # Plot the function
        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, label="Function", color="blue")
        ax.scatter(results[0], results[1], color="red", label="Extrema")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Local Extrema")
        ax.legend()
        st.pyplot(fig)