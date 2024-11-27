import streamlit as st
import numpy as np

def data_point_x(m):
    A = []
    columns = st.columns(m)
    for i in range(m):
        with columns[i]:
            A.append(st.number_input(f'$(x)$[{i + 1}]', value=None,format="%f",min_value=.00000001, key=f'$(x)$[{i + 1}]'))
    return A

def data_point_fx(m):
    A = []
    columns = st.columns(m)
    for i in range(m):
        with columns[i]:
            A.append(st.number_input(f'$(fx)$[{i + 1}]', value=None,format="%f",min_value=.00000001, key=f'$(f(x))[{i + 1}]'))
    return A
