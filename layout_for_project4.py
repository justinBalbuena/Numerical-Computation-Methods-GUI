import streamlit as st
import numpy as np
import pandas as pd
from functions.Cramer_Rule import crammer_rule


def run_page_4():
    st.title("Cramer Rule")
    st.write("Enter the row and columns for augmented matrix")
    st.write("For example, for a system of 2 equations with 2 variables, you would enter a 2x3 matrix.")
    #all wrapped in a form which looks like a box on the actual website
    matrix_form = st.form(key='matrix_form')
    rows = matrix_form.number_input("Number of rows", min_value=1, step=1)
    column = matrix_form.number_input("Number of column", min_value=1, step=1)
    #3 1 4 7 -2 3 1 -5 2 0 5 10 quick numbers to test 3x4 matrix
    user_matrix = matrix_form.text_input("Enter the Augmented Matrix (use space to divide): ")

    pressed = matrix_form.form_submit_button("Evaluate")
    if pressed:
        #I forgor but make a list out of the text input from the form
        numbers = list(map(float,user_matrix.split()))
        #reshapes the list to make a matrix
        matrix_a = np.matrix(numbers).reshape(rows, column)

        matrix_b = matrix_a[:, column - 1]
        matrix_a = np.delete(matrix_a, column - 1, 1)
        solution = crammer_rule(matrix_a, matrix_b)
        #this is the graph looking thing in the page
        df_a = pd.DataFrame(matrix_a)
        df_b = pd.DataFrame(matrix_b)
        if solution != False:
            st.write("Matrix A: ",df_a,"Matrix B: ",df_b,"the solution is: ",solution)

