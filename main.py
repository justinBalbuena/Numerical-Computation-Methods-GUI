import streamlit as st
from page_layout.home_page import home_page
from page_layout.bisection_page_layout import bisection_page_layout
#must download streamlit option menu package 4.0

#Before coding, run the file first to familiarize with what is happening and to fully understand the comments

#nav bar is the thing on top center when running the file

#IF FIRST TIME VIEW PLEASE SKIP TO LINE 71

#this just makes the page wider
st.set_page_config(layout="wide")

#function for the home section
def home():
    st.title("Overview")
    st.write("Welcome! This is a simple GUI (Graphic User Interface) that preforms varies types of numerical methods. Please write more?")
# -------------------------------------------------------------------------------------------------#

#section for the root finding method nav bar
def bisection_method():
    #this runs the file page_layout > bisection_page_layout
    bisection_page_layout()
def false_position_method():
    st.title("False Position Method")
def secant_method():
    st.title("Secant Method")
def newton_method():
    st.title("Newton Method")
#-------------------------------------------------------------------------------------------------#

#Functions for linear Algebraic section on the nav bar
def gaussian_directed_elimination():
    st.title("Gaussian Directed Elimination")
def gaussian_jordan_directed_elimination():
    st.title("Gaussian Jordan Directed Elimination")
def gauss_seidel_iterative_method():
    st.title("Gaussian Seidel Iterative Method")
def jacobi_iterative_method():
    st.title("Jacobi Iterative Method")
#-------------------------------------------------------------------------------------------------#

#functions for Numerical Differentiation section in nav bar
def lagrange_interpolation():
    st.title("Lagrange Interpolation")
def two_point_forward_formula():
    st.title("Two Point Forward Formula")
def three_point_center_formula():
    st.title("Three Point Center Formula")
def three_point_forward_formula():
    st.title("Three Point Forward Formula")
#-------------------------------------------------------------------------------------------------#

#functions for Numerical Integration section in nav bar
def trapezoidal_rule_ma():
    st.title("Multiple Application of the Trapezoidal Rule")
def simpson_rule_c():
    st.title("Composite Simpson's Rule")

#-------------------------------------------------------------------------------------------------#

#function for non-linear optimization section in nav bar
def golden_section_method():
    st.title("Golden Section Method")
def nl_newton_method():
    st.title("Newton Method (with an automatic evaluation of a corresponding derivative)")

#-------------------------------------------------------------------------------------------------#

#Read this First Section
#this serves as a type of array that stores the function within the names in green
#these function are located above and will be where you run your files

root_finding_methods = {
    "Bisection Method": bisection_method,
    "False-Position Method": false_position_method,
    "Secant Method": secant_method,
    "Newton Method": newton_method
}
linear_algebraic_methods = {
    "Gaussian directed Elimination": gaussian_directed_elimination,
    "Gaussian-Jordan directed Elimination": gaussian_jordan_directed_elimination,
    "Gauss-Seidel iterative Method": gauss_seidel_iterative_method,
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
#-------------------------------------------------------------------------------------------------#

#this is the nav bar located in page_layout > home_page() if possible maybe could use more css
homepage = home_page()
#-------------------------------------------------------------------------------------------------#

#get familiar with the syntax as it is crucial to use the file page_layout > error_option
#syntax is located root_finding_methods.keys() and line 115
#people with flag will have to change to a b c d system

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