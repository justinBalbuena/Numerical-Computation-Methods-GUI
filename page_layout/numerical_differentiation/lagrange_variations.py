import streamlit as st
from global_functions_and_more.format_functions import x_y_field
from functions.melvin.lagrange_diff import numdef
from functions.Ant.numerical_diff.points_numerical import PtsFwdAndCenter

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

    # error
    usererror = st.text_input(label="**:green[Error Tolerance Value]**: ", key="users_error_value")

    # Number of columns input
    columns = st.text_input(label="**:green[Columns]**: ", key="amount_of_columns")

    wanted_value = st.text_input(label="**:green[Wanted Value to Differentiate]**: ", key="users_wanted_value")
    # Only create fields if `columns` is a valid integer
    if columns and columns.isdigit() and wanted_value and usererror:
        columns = int(columns)
        st.session_state["columns"] = columns  # Save the columns count in session state

        st.session_state["diffform"] = choices[selected_option]

        usererr = float(usererror)
        st.session_state["usererror"] = usererr

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

            wanted = st.session_state["wanted_value"]
            inerror = st.session_state["usererror"]
            diffch = st.session_state["diffform"]
            st.markdown(
                f"""
                        <style>
                        .focus_highlight {{
                            color: green;
                        }}
                        </style>

                        <h4>
                            The differentiated value at <span class="focus_highlight">{st.session_state["wanted_value"]}</span> is: <span class="focus_highlight">{PtsFwdAndCenter(wanted_value,x_arr, y_arr, inerror, diffch, "Cubic")}</span>
                        </h4>

                    """,
                unsafe_allow_html=True
            )