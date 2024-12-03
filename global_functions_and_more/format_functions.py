import streamlit as st


def matrix_field(rows, columns):
    count = 1
    index = None
    for i in range(0, rows):
        # Initialize a new row
        cols_inputs = st.columns(columns)

        for index, col in enumerate(cols_inputs):
            col.text_input(label=f"Cell {count}:", key=f"matrix_square_{count}")
            count += 1


def x_y_field(columns):
    count = 1
    index = None
    for i in range(0, 2):
        # Initialize a new row
        cols_inputs = st.columns(columns)

        for index, col in enumerate(cols_inputs):
            col.text_input(label=f"Cell {count}:", key=f"input_field_{count}")
            count += 1