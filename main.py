import streamlit as st
from streamlit_option_menu import option_menu

from page_layout.home_page import home_page
from page_layout.bisection_page_layout import bisection_page_layout
#must download streamlit option menu package 4.0

from functions.Ant.bisection import ant_bisection_method, find_roots

st.set_page_config(layout="wide")
# Define the different pages as functions
def home():
    st.title("Overview")
    st.write("Welcome! This is a simple GUI (Graphic User Interface) that preforms varies types of numerical methods. Please write more?")
#Functions for root finding method

def bisection_method():
    bisection_page_layout()
def false_position_method():
    st.title("False Position Method")
def secant_method():
    st.title("Secant Method")
def newton_method():
    st.title("Newton Method")

#Functions for linear Algebraic
def gaussian_directed_elimination():
    st.title("Gaussian Directed Elimination")
def gaussian_jordan_directed_elimination():
    st.title("Gaussian Jordan Directed Elimination")
def gauss_seidel_iterative_method():
    st.title("Gaussian Seidel Iterative Method")
def jacobi_iterative_method():
    st.title("Jacobi Iterative Method")
#test again
#functions for Numerical Diff
def lagrange_interpolation():
    st.title("Lagrange Interpolation")
def two_point_forward_formula():
    st.title("Two Point Forward Formula")
def three_point_center_formula():
    st.title("Three Point Center Formula")
def three_point_forward_formula():
    st.title("Three Point Forward Formula")

#functions for Numerical Integration
def trapezoidal_rule_ma():
    st.title("Multiple Application of the Trapezoidal Rule")
def simpson_rule_c():
    st.title("Composite Simpson's Rule")

#function for non-linear optimization
def golden_section_method():
    st.title("Golden Section Method")
def nl_newton_method():
    st.title("Newton Method (with an automatic evaluation of a corresponding derivative)")


homepage = {
    "Home": home,
}
root_finding_methods = {
    "Bisection Method": bisection_method,
    "False-Position Method": false_position_method,
    "Secant Method": secant_method,
    "Newton Method": newton_method
}
linear_algebraic_methods = {
    "Gaussian directed Elimination": gaussian_directed_elimination,
    "Gaussian-Jordan directed Elimination": gaussian_jordan_directed_elimination,
    "Gauss-Seidel iterative Method": gauss_seidel_iterative_Method,
    "Jacobi iterative Method": jacobi_iterative_method
}
Numerical_diff = {
    "Lagrange Interpolation": lagrange_interpolation,
    "Two point forward difference formula": two_point_forward_formula,
    "Three point center difference formula": three_point_center_formula,
    "Three point forward difference formula": three_point_forward_formula,
}
Numerical_int = {
    "Trapezoidal rule (multiple application)" : trapezoidal_rule_ma,
    "Simpson's rule (Composite)": simpson_rule_c,
}
Non_linear_opti = {
    "Golden Section Method": golden_section_method,
    "Newton Method": nl_newton_method
}

homepage = home_page()
if homepage == "Home":
    home()
if homepage == "Root-Finding Methods":
    r_f_m = st.selectbox("Select Root Finding Method",root_finding_methods.keys())
    root_finding_methods[r_f_m]()
if homepage == "Linear Algebraic Equations":
    l_a_e = st.selectbox("Select Numerical linear algebraic equations Method",linear_algebraic_methods.keys())
    linear_algebraic_methods[l_a_e]()
if homepage == "Numerical Differentiation":
    n_d = st.selectbox("Select Numerical differentiation Method",Numerical_diff.keys())
    Numerical_diff[n_d]()
if homepage == "Numerical Integration":
    n_i= st.selectbox("Select Numerical Integration Method",Numerical_int.keys())
    Numerical_int[n_i]()
if homepage == "Non-Linear Optimization":
    n_l_o = st.selectbox("Select Non-Linear Optimization Method",Non_linear_opti.keys())
    Non_linear_opti[n_l_o]()


