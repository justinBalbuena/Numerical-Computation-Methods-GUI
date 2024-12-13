import streamlit as st
from global_functions_and_more.format_functions import x_y_field
from functions.Ant.numerical_integration.simpson import simpson_rule


def composite_simpson_page_layout():
    # Composite Simpson's Rule
    st.title("Composite Simpson's Rule")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("More accurate estimate of an integral is obtained if a higher-order polynomial is used to connect the points. The formulas that result from taking the integrals under such polynomials are called Simpson’s rules")
    st.write("Divide the interval into n sub-intervals and apply Simpson’s Rule on each consecutive pair of sub-intervals. Note that n must be even")
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

    nvals = st.text_input(label="**:green[Enter number of intervals]**: ", key="users_n_values")
    # Number of columns input
    columns = st.text_input(label="**:green[Columns]**: ", key="amount_of_columns")




    # Only create fields if `columns` is a valid integer
    if columns and columns.isdigit() and hval:
        columns = int(columns)
        st.session_state["columns"] = columns  # Save the columns count in session state

        nvals = int(nvals)
        st.session_state["nvals"] = nvals

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

            res = {x_arr[i]: y_arr[i] for i in range(len(x_arr))}
            usern = st.session_state["nvals"]
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
                            The integrated value is: <span class="focus_highlight">{simpson_rule(x_arr,y_arr,hv)}</span>
                        </h4>

                    """,
                unsafe_allow_html=True
            )


