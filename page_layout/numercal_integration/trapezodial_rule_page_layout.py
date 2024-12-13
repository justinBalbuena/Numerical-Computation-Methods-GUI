import streamlit as st
from global_functions_and_more.format_functions import x_y_field
from functions.justin.project9.trapezoidal_rule import trapezoidal_rule


def trapezoidal_rule_page_layout():
    # Composite Simpson's Rule
    st.title("Multiple Application of Trapezoidal Rule")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("One way to improve the accuracy of the trapezoidal rule is to divide the integration interval from a to b into a number of equal segments of the length h and apply the method to each segment")
    st.write("The areas of individual segments can then be added to yield the integral for the entire interval")
    # Calculation Section

    st.header("Calculation", divider="blue")



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
                    <h4 class="text">Please be sure to have an even sized input </h4>
                </div>
            """,
        unsafe_allow_html=True
    )


    # error
    hval = st.text_input(label="**:green[Enter H value]**: ", key="users_h_value")

    # Number of columns input
    columns = st.text_input(label="**:green[Columns]**: ", key="amount_of_columns")


    # Only create fields if `columns` is a valid integer
    if columns and columns.isdigit() and hval:
        columns = int(columns)
        st.session_state["columns"] = columns  # Save the columns count in session state

        hv = float(hval)
        st.session_state["hval"] = hv

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
            #wanted = st.session_state["wanted_value"]

            res = {x_arr[i]:y_arr[i] for i in range(len(x_arr))}

            inh = st.session_state["hval"]
            # Results Section
            st.header("Results", divider="blue")
            st.markdown(
                f"""
                        <style>
                        .focus_highlight {{
                            color: green;
                        }}
                        </style>

                        <h4>
                            The integrated value is: <span class="focus_highlight">{trapezoidal_rule(res, inh)}</span>
                        </h4>

                    """,
                unsafe_allow_html=True
            )


