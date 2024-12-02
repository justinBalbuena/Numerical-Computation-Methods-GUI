import streamlit as st

from page_layout.numercal_integration.composite_simpson_page_layout import composite_simpson_page_layout
from page_layout.non_linear_optimization.golden_section_page_layout import golden_section_page_layout
from page_layout.home_page import home_page
from page_layout.root_finding_methods.bisection_page_layout import bisection_page_layout
from page_layout.root_finding_methods.false_position_page_layout import false_position_page_layout
from page_layout.linear_algebraic_equations.jacobi_method_page_layout import jacobi_method_page_layout
from page_layout.non_linear_optimization.newton_op_page_layout import newton_op_page_layout
from page_layout.root_finding_methods.secant_page_layout import secant_page_layout
from page_layout.root_finding_methods.newton_method_page_layout import newton_method_page_layout
from page_layout.linear_algebraic_equations.gaussian_d_elimination_page_layout import gaussian_d_elimination_page_layout
from page_layout.linear_algebraic_equations.gauss_jordan_d_elimination_page_layout import gauss_jordan_d_elimination_page_layout
from page_layout.linear_algebraic_equations.gauss_seidel_page_layout import gauss_seidel_page_layout
from page_layout.numerical_differentiation.lagrange_interpolation_page_layout import lagrange_interpolation_page_layout
from page_layout.numercal_integration.trapezodial_rule_page_layout import trapezoidal_rule_page_layout
from page_layout.numerical_differentiation.two_p_f_d_page_layout import two_point_forward_page_layout
from page_layout.numerical_differentiation.three_p_c_d_page_layout import three_point_center_page_layout
from page_layout.numerical_differentiation.three_p_f_d_page_layout import three_points_forward_page_layout
from page_layout.linear_algebraic_equations.cramer_page_layout import cramer_page_layout
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

#section for the root finding method nav bar. All have the similar format found in bisection method
def bisection_method():
    #this runs the file page_layout > bisection_page_layout
    bisection_page_layout()
def false_position_method():
    false_position_page_layout()
def secant_method():
    secant_page_layout()
def newton_method():
    newton_method_page_layout()
#-------------------------------------------------------------------------------------------------#

#Functions for linear Algebraic section on the nav bar
def gaussian_directed_elimination():
    gaussian_d_elimination_page_layout()
def gaussian_jordan_directed_elimination():
    gauss_jordan_d_elimination_page_layout()
def gauss_seidel_iterative_method():
    gauss_seidel_page_layout()
def jacobi_iterative_method():
    jacobi_method_page_layout()
def cramer_method():
    cramer_page_layout()
#-------------------------------------------------------------------------------------------------#

#functions for Numerical Differentiation section in nav bar
def lagrange_interpolation():
    lagrange_interpolation_page_layout()
def two_point_forward_formula():
    two_point_forward_page_layout()
def three_point_center_formula():
    three_point_center_page_layout()
def three_point_forward_formula():
    three_points_forward_page_layout()
#-------------------------------------------------------------------------------------------------#

#functions for Numerical Integration section in nav bar
def trapezoidal_rule_ma():
    trapezoidal_rule_page_layout()
def simpson_rule_c():
    composite_simpson_page_layout()

#-------------------------------------------------------------------------------------------------#

#function for non-linear optimization section in nav bar
def golden_section_method():
    golden_section_page_layout()

def nl_newton_method():
    newton_op_page_layout()
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
    "Gaussian Elimination": gaussian_directed_elimination,
    "Gaussian-Jordan Elimination": gaussian_jordan_directed_elimination,
    "Gauss-Seidel iterative Method": gauss_seidel_iterative_method,
    "Jacobi iterative Method": jacobi_iterative_method,
    "Cramer's Rule":cramer_method
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