import streamlit as st
from global_functions_and_more.format_functions import x_y_field
from functions.Shirley.Project_8 import lagrange_variation
from functions.Shirley.Project_8.lagrange_variation import lagrange_variation

def lagrange_variations_layout():
    st.title("Numerical Differentiation")
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
            <h4 class="text">Please select what type of rule you would like to use</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Options for derivative methods
    options = ["2 points forward", "3 points forward", "3 points centered"]
    selected_option = st.selectbox("Choose an option:", options)
    st.write(f"You selected: {selected_option}")

    # Mapping options to flags
    flag = {
        "2 points forward": "a",
        "3 points forward": "b",
        "3 points centered": "c"
    }
    selected_flag = flag[selected_option]

    # User inputs
    usererror = st.text_input(label="**:green[Error Tolerance Value]**:", key="users_error_value")
    columns = st.text_input(label="**:green[Columns]**:", key="amount_of_columns")
    val = st.text_input(label="**:green[Wanted Value to Differentiate]**:", key="users_wanted_value")

    # Ensure inputs are valid
    if columns and columns.isdigit() and val and usererror:
        try:
            columns = int(columns)
            h = float(usererror)
            val = float(val)

            st.session_state["columns"] = columns
            st.session_state["usererror"] = h
            st.session_state["wanted_value"] = val
            st.session_state["diffform"] = selected_flag

            # Generate input fields for x and y values
            x_y_field(columns)

            if st.button("Input Values"):
                x_arr = [st.session_state.get(f"input_field_{i}", "") for i in range(1, columns + 1)]
                y_arr = [st.session_state.get(f"input_field_{i}", "") for i in range(columns + 1, 2 * columns + 1)]

                # Convert to float and validate
                try:
                    x_arr = [float(x) for x in x_arr]
                    y_arr = [float(y) for y in y_arr]

                    # Ensure arrays match in length
                    if len(x_arr) != len(y_arr):
                        st.error("The lengths of x and y arrays must match.")
                        return

                    # Call the Lagrange variation function
                    derivative = lagrange_variation(val, x_arr, y_arr, selected_flag, h)

                    # Display the result
                    st.markdown(
                        f"""
                        <style>
                        .focus_highlight {{
                            color: green;
                        }}
                        </style>
                        <h4>
                            The differentiated value at <span class="focus_highlight">{val}</span> is: <span class="focus_highlight">{derivative}</span>
                        </h4>
                        """,
                        unsafe_allow_html=True
                    )

                except ValueError as e:
                    st.error(f"Error converting inputs: {e}")

        except ValueError as e:
            st.error(f"Error parsing inputs: {e}")
    else:
        st.warning("Please provide valid inputs for all fields.")
