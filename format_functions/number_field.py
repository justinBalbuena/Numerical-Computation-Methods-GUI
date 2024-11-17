import streamlit as st


def number_field(rows, columns):
    index = None
    for i in range(1, rows+1):
        # Initialize a new row
        cols_inputs = st.columns(columns)

        for col in cols_inputs:
            col.markdown(
                f"""
                    <style>
                    </style>
                    <h4>
                    </h4>
                """,
                unsafe_allow_html=True
            )
            col.text_input(label="Input:", key=f"matrix_square_{()}")

