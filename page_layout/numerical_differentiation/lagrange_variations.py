import streamlit as st
from global_functions_and_more.format_functions import x_y_field
from functions.justin.project8.langrange_with_diff import lagrange_with_diff


def lagrange_variations_layout():
    st.title("Numerical Differentiation")
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
                    <h4 class="text">Please select what type of rule you would like to use </h4>
                </div>
            """,
        unsafe_allow_html=True
    )
    options = ["2 points forward", "3 points forward", "3 points centered"]

    # Create the selection box
    selected_option = st.selectbox("Choose an option:", options)

    # Display the selected option
    st.write(f"You selected: {selected_option}")

    choices = {
        "2 points forward": "a",
        "3 points forward": "b",
        "3 points centered": "c"
    }

    quad_or_cub = {
        "Quadratic": "quadratic",
        "Cubic": "cubic"
    }

    interp_type = st.radio("Quadratic or Cubic Interpolation: ", quad_or_cub.keys())
    type = quad_or_cub[interp_type]

    # Step Value
    step_value = st.number_input(label="**:green[Step Value]**: ", key="users_step_value")

    # Number of columns input
    columns = st.text_input(label="**:green[Columns]**: ", key="amount_of_columns")

    wanted_value = st.text_input(label="**:green[Wanted Value to Differentiate]**: ", key="users_wanted_value")
    # Only create fields if `columns` is a valid integer
    if columns and columns.isdigit() and wanted_value and step_value:
        columns = int(columns)
        st.session_state["columns"] = columns  # Save the columns count in session state

        st.session_state["diffform"] = choices[selected_option]

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
            my_dict = dict(zip(x_arr, y_arr))


            wanted = st.session_state["wanted_value"]
            diffch = st.session_state["diffform"]

            print(my_dict, step_value, wanted, diffch, type)
            st.markdown(
                f"""
                        <style>
                        .focus_highlight {{
                            color: green;
                        }}
                        </style>

                        <h4>
                            The differentiated value at <span class="focus_highlight">{wanted}</span> is: <span class="focus_highlight">{lagrange_with_diff(my_dict, step_value, wanted, diffch, type)}</span>
                        </h4>

                    """,
                unsafe_allow_html=True
            )