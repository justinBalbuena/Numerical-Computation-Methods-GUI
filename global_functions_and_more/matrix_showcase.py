import streamlit as st
import numpy as np
import pandas as pd

######################
# Remove the column index
######################
def remove_column_index(latex_matrix):
    # Find the \top rule index
    top_rule_index = latex_matrix.find(r'\toprule')
    # Find the \midrule index
    mid_rule_index = latex_matrix.find(r'\midrule')
    # Remove the string between \toprule and \midrule
    latex_matrix = latex_matrix[:top_rule_index] + latex_matrix[mid_rule_index + 8:]
    # Find the \bottomrule index
    bottom_rule_index = latex_matrix.find(r'\bottomrule')
    # Remove the second character before \bottomrule until \bottomrule
    latex_matrix = latex_matrix[:bottom_rule_index - 2] + latex_matrix[bottom_rule_index + 11:]
    return latex_matrix


######################
# Function for matrix number 1
######################
def display_matrix(matrix):
    df = pd.DataFrame(matrix)

    # Convert the dataframe to KaTeX format
    latex_matrix = df.to_latex(index=False, escape=False, )
    latex_matrix = remove_column_index(latex_matrix)

    # Round the numbers
    latex_matrix = latex_matrix.replace('.000000', '').replace('.000', '').replace('.00', '')

    # Clean the latex_matrix
    latex_matrix = latex_matrix.replace(r'\begin{tabular}', r'\begin{bmatrix}').replace(r'\end{tabular}',r'\end{bmatrix}'.replace(r'\hline', '')).replace(r'\\', r'\\ \,')

    # Find the index of '{r' until '}' and replace it with ''
    while latex_matrix.find('{r') != -1:
        start = latex_matrix.find('{r')
        end = latex_matrix.find('}', start) + 1
        latex_matrix = latex_matrix[:start] + latex_matrix[end:]

    # Display the matrix using KaTeX
    st.latex(latex_matrix)


def matrix_menu(m,n):
    A = []
    sub_columns = st.columns(n)
    for i in range(m):
        for j in range(n):
            with sub_columns[j]:
                A.append(st.number_input(f'A[{i + 1},{j + 1}]', value=0, key=f'A[{i + 1},{j + 1}]'))

    # Create a dataframe matrix from the input
    custom_matrix = np.array(A).reshape(m,n)
    return custom_matrix

