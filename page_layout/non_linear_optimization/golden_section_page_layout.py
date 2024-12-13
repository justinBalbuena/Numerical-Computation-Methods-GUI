import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sympy import lambdify, symbols, Symbol

from global_functions_and_more.convert_mathexpression import transform_math_expression
from global_functions_and_more.error_option import extrema_types
from functions.Shirley.Project_10.Golden_Section import golden_section


def golden_section_page_layout():
    """
    Streamlit layout for Golden Section Method
    """
    # Title and description
    st.title("Golden Section Method")
    st.markdown("This page allows you to find the minimum or maximum of a function using the Golden Section method.")

    # Input section
    st.header("Inputs", divider="blue")
    golden_section_form = st.form(key="golden_section_form")
    function = golden_section_form.text_input("Enter a function (e.g., 2*sin(x)-exp(x)/4-1):")
    extrema_type = golden_section_form.radio("Extrema Type:", extrema_types.keys())
    flag = extrema_types[extrema_type]()
    left_bracket = golden_section_form.number_input("Enter the left bracket:", value=0.0, format="%f")
    right_bracket = golden_section_form.number_input("Enter the right bracket:", value=1.0, format="%f")
    tolerance = golden_section_form.number_input("Enter the tolerance value:", value=0.001, format="%f")

    pressed = golden_section_form.form_submit_button("Evaluate")

    if pressed:
        try:
            # Convert function string to callable function
            x = Symbol('x')  # Symbol for lambdification
            symbolic_function = transform_math_expression(function)  # Convert string to symbolic expression
            f = lambdify(x, symbolic_function)  # Create a callable function from the symbolic expression

            # Perform the golden section search
            result = golden_section(left_bracket, right_bracket, f, (1 + np.sqrt(5)) / 2, tolerance)

            # Display results
            st.subheader("Results")
            if flag:  # Maxima
                st.write(f"The maximum value is at x = {result[0]:.4f}")
                st.write(f"Function value at the maximum: f(x) = {result[1]:.4f}")
            else:  # Minima
                st.write(f"The minimum value is at x = {result[0]:.4f}")
                st.write(f"Function value at the minimum: f(x) = {result[1]:.4f}")
            st.write(f"Number of iterations: {result[2]}")

            # Plotting
            st.subheader("Function Plot")
            x_values = np.linspace(left_bracket, right_bracket, 500)
            y_values = [f(val) for val in x_values]

            fig, ax = plt.subplots()
            ax.plot(x_values, y_values, label="Function", color="blue")
            ax.scatter(result[0], result[1], color="red", label="Extrema")
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            ax.set_title(f"{extrema_type} of the Function")
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    golden_section_page_layout()