import streamlit as st

from functions.Ant.lagrange_method import ant_lagrange
from global_functions_and_more.data_points import data_point_fx,data_point_x

def lagrange_interpolation_page_layout():
    # Lagrange Interpolation
    st.title("Lagrange Interpolation")
    # Theorem section
    st.header("Theorem", divider="blue")
    st.write("The Lagrange interpolating polynomial is simply a reformulation of the Newton’s polynomial avoiding the computation of divided differences:")
    # Calculation Section
    st.header("Calculation", divider="blue")
    x = st.number_input("What Point are you looking for?", value=None)
    n = st.number_input("data set value ${x}$(max is 10)", min_value=1,max_value=10,value=1, key='n')
    data_value = data_point_x(n)
    m = st.number_input('data function value ${fx}$(max is 10)', min_value=1, max_value = 10,value=1, key='m')
    data_set = data_point_fx(m)
    pressed = st.button("Evaluate")
    if m != n:
        st.write("both the values in x and fx must be the same")
    else:
        if pressed:
            result = ant_lagrange(x,data_value,data_set)
            st.write(result)

