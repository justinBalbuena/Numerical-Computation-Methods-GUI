import streamlit as st
import matplotlib.pyplot as plt
from global_functions_and_more.convert_mathexpression import transform_math_expression
from global_functions_and_more.error_option import extrema_types
from functions.justin.project10.golden_section import golden_section

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
        results = golden_section(left_bracket, right_bracket, function, flag, tolerance)
        st.write(f"The x value of the local extrema is: **:blue[{results[0]}]**")
        st.write(f"The y value of the local extrema is: **:blue[{results[1]}]**")
        st.write(f"The amount of iterations it took was: **:blue[{results[2]}]**")

        #Graph Section
        fig, ax = plt.subplots()
        ax.scatter(results[0], results[1], color='red')
        ax.set_xlabel('X values')
        ax.set_ylabel('Y values')
        ax.set_title('Local Extrema:')
        ax.legend()
        st.pyplot(fig)