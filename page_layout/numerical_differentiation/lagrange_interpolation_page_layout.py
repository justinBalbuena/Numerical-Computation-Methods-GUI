from functions.justin.project7.lagrange_interpolation import lagrange_interpolation
from global_functions_and_more.format_functions import x_y_field
import streamlit as st


def lagrange_interpolation_page_layout():
    # Lagrange Interpolation
    st.title("Lagrange Interpolation")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("The Lagrange interpolating polynomial is simply a reformulation of the Newton’s polynomial avoiding the computation of divided differences:")
    # Calculation Section

    st.markdown(
        f"""
                <style>
                    .size_box {{
                        justify-content: center;
                        align-items: center;
                    }}
                    .text {{
                        padding-top: 16px;
                        padding-bottom: 16px;
                    }}
                </style>
                <div class="size_box">
                    <h4 class="text">Please enter how many set of values you would like to put</h4>
                </div>
            """,
        unsafe_allow_html=True
    )

    # Number of columns input
    columns = st.text_input(label="**:blue[Columns]**: ", key="amount_of_columns")
    wanted_value = st.text_input(label="**:blue[Wanted Value to Interpolate]**: ", key="users_wanted_value")
    # Only create fields if `columns` is a valid integer
    if columns and columns.isdigit() and wanted_value:
        columns = int(columns)
        st.session_state["columns"] = columns  # Save the columns count in session state

        wanted_value = float(wanted_value)
        st.session_state["wanted_value"] = wanted_value

        # Dynamically generate x and y input fields based on the number of columns
        x_y_field(columns)

        # Collect values in x and y arrays when the "Input Values" button is clicked
        if st.button("Input Values"):
            st.session_state["x_arr"] = [st.session_state.get(f"input_field_{i}", "") for i in
                                         range(1, columns + 1)]
            st.session_state["y_arr"] = [st.session_state.get(f"input_field_{i}", "") for i in
                                         range(columns + 1, 2 * columns + 1)]

            x_arr = [float(x) for x in st.session_state["x_arr"]]
            y_arr = [float(y) for y in st.session_state["y_arr"]]

            st.markdown(
                f"""
                        <style>
                        .focus_highlight {{
                            color: #60b4f0;
                        }}
                        </style>

                        <h4>
                            The interpolated value at <span class="focus_highlight">{st.session_state["wanted_value"]}</span> is: <span class="focus_highlight">{lagrange_interpolation(x_arr, y_arr, st.session_state["wanted_value"])}</span>
                        </h4>

                    """,
                unsafe_allow_html=True
            )

