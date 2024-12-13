import streamlit as st
from global_functions_and_more.format_functions import x_y_field
from functions.Shirley.Project_9.Simpsons_rule import simpsons_rule

def composite_simpson_page_layout():
    # Composite Simpson's Rule
    st.title("Composite Simpson's Rule")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write(
        "More accurate estimate of an integral is obtained if a higher-order polynomial is used to connect the points. The formulas that result from taking the integrals under such polynomials are called Simpson’s rules.")
    st.write(
        "Divide the interval into \(n\) sub-intervals and apply Simpson’s Rule on each consecutive pair of sub-intervals. Note that \(n\) must be even.")

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
            <h4 class="text">Please ensure the number of intervals is even and inputs are correct.</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Input fields for `h` and number of intervals
    hval = st.text_input(label="**:green[Enter H value (step size)]**: ", key="users_h_value")
    nvals = st.text_input(label="**:green[Enter number of intervals (n, must be even)]**: ", key="users_n_values")
    columns = st.text_input(label="**:green[Number of Data Points]**: ", key="amount_of_columns")

    # Ensure input validity
    if columns and columns.isdigit() and hval and nvals:
        columns = int(columns)
        st.session_state["columns"] = columns
        hv = float(hval)
        st.session_state["hval"] = hv
        nvals = int(nvals)
        st.session_state["nvals"] = nvals

        # Dynamically generate x and y input fields based on the number of columns
        x_y_field(columns)

        # Collect values in x and y arrays when the "Input Values" button is clicked
        if st.button("Input Values"):
            st.session_state["x_arr"] = [st.session_state.get(f"input_field_{i}", "") for i in range(1, columns + 1)]
            st.session_state["y_arr"] = [st.session_state.get(f"input_field_{i}", "") for i in
                                         range(columns + 1, 2 * columns + 1)]

            try:
                x_arr = [float(x) for x in st.session_state["x_arr"]]
                y_arr = [float(y) for y in st.session_state["y_arr"]]

                # Create the dictionary for fx
                fx = {x_arr[i]: y_arr[i] for i in range(len(x_arr))}

                # Call Simpson's Rule function
                result = simpsons_rule(hv, fx)

                # Results Section
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
            except ValueError as e:
                st.error(f"Error: {str(e)}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")
