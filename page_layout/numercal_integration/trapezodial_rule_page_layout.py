import streamlit as st
from global_functions_and_more.format_functions import x_y_field
from functions.Shirley.Project_9.Trapezoidal_rule import trapezoidal_rule
from functions.Shirley.Project_9 import Trapezoidal_rule

def trapezoidal_rule_page_layout():
    # Composite Trapezoidal Rule
    st.title("Multiple Application of Trapezoidal Rule")

    # Theorem Section
    st.header("Theorem", divider="blue")
    st.write(
        "One way to improve the accuracy of the trapezoidal rule is to divide the integration interval from a to b into a number of equal segments of the length h and apply the method to each segment.")
    st.write("The areas of individual segments can then be added to yield the integral for the entire interval.")

    # Calculation Section
    st.header("Calculation", divider="blue")
    st.markdown(
        """
        <style>
            .size_box {
                justify-content: center;
                align-items: center;
            }
            .text {
                padding-top: 16px;
                padding-bottom: 16px;
            }
        </style>
        <div class="size_box">
            <h4 class="text">Please be sure to have an even-sized input for accurate results.</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Input Fields
    hval = st.text_input(label="**:green[Enter Step Size (h)]**:", key="users_h_value")
    columns = st.text_input(label="**:green[Number of Points]**:", key="amount_of_columns")

    if columns and columns.isdigit() and hval:
        columns = int(columns)
        hval = float(hval)

        # Generate input fields for x and y values
        st.markdown("### Input X and Y Values")
        x_values = []
        y_values = []

        for i in range(columns):
            col1, col2 = st.columns(2)
            with col1:
                x_val = st.text_input(f"Enter X[{i + 1}]:", key=f"x_input_{i}")
                x_values.append(x_val)
            with col2:
                y_val = st.text_input(f"Enter Y[{i + 1}]:", key=f"y_input_{i}")
                y_values.append(y_val)

        if st.button("Calculate"):
            try:
                # Convert input strings to floats
                x_values = [float(x) for x in x_values if x]
                y_values = [float(y) for y in y_values if y]

                # Ensure inputs are valid
                if len(x_values) != columns or len(y_values) != columns:
                    st.error("Please enter all X and Y values.")
                else:
                    # Create fx dictionary
                    fx = {x_values[i]: y_values[i] for i in range(columns)}

                    # Call trapezoidal_rule function
                    result = trapezoidal_rule(hval, fx)

                    # Display Result
                    st.header("Results", divider="blue")
                    st.markdown(
                        f"""
                        <style>
                        .focus_highlight {{
                            color: green;
                            font-weight: bold;
                        }}
                        </style>
                        <h4>
                            The integrated value is: <span class="focus_highlight">{result}</span>
                        </h4>
                        """,
                        unsafe_allow_html=True
                    )
            except ValueError:
                st.error("Ensure all inputs are numeric.")
