import streamlit as st
from streamlit_option_menu import option_menu
#must download streamlit option menu package 4.0

#from functions.Ant.bisection import ant_bisection_method


st.set_page_config(layout="wide")
# Define the different pages as functions
def home():
    st.title("Overview")
    st.write("Welcome! This is a simple GUI (Graphic User Interface) that preforms varies types of numerical methods. Please write more?")

#Functions for root finding method
def bisection_method():
    st.title("Bisection Method")
    #Explain the Theorem
    st.header("Theorem",divider="blue")
    st.write("An equation f(x)=0, where f(x) is a real continuous function, has at least one root between x1 and x2 if f(x1) f(x2) < 0 (the function changes sign on opposite sides of the root)")
    st.write("So at least one root of the equation f(x)=0 exists between the two points if the function f(x) is real, continuous, and changes sign on the interval [x1,x2]")
    #this is calculation section
    st.header("Calculation",divider="blue")
    #Calculation Section
    error_method = st.radio("Error Tolerance Method",error_tolerance_methods.keys())
    result = error_tolerance_methods[error_method]()
    st.text_input("Enter a function Ex(2*sin(x)) or 2**3 for powers")
    x1 = st.number_input(label="Enter a value for x1")
    x2 = st.number_input(label="Enter a value for x2")
    tolerance = st.number_input(label="Tolerance value (absolute values will be used)")




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
def gauss_seidel_iterative_Method():
    st.title("Gaussian Seidel Iterative Method")
def jacobi_iterative_method():
    st.title("Jacobi Iterative Method")

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

def absolute_error_method():
    return "a"
def relative_error_method():
    return "b"
def true_absolute_error_method():
    return "c"
def combination():
    return "d"

#Function for
# page_names_to_funcs = {
#     "Home": home,
#     "Project 1": project1,
#     "Project 2": project2,
#     "Project 3": project3,
#     "Project 4": project4,
#     "Project 5": project5,
#     "Project 6": project6,
#     "Project 7": project7,
#     "Project 8": project8,
#     "Project 9": project9
# }
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
error_tolerance_methods = {
    "Absolute Error": absolute_error_method,
    "Relative Error": relative_error_method,
    "True Absolute Error": true_absolute_error_method,
    "Combination of Absolute Error and Relative Error": combination
}
# home_page = st.sidebar.button("Home")
# S1 = st.sidebar.selectbox("Root-Finding Methods",root_finding_methods.keys())
# S2 = st.sidebar.selectbox("Numerical linear algebraic equations",linear_algebraic_methods)
# S3 = st.sidebar.selectbox("Numerical Differentiation",Numerical_diff)
# S4 = st.sidebar.selectbox("Numerical Integration",Numerical_int)
# S5 = st.sidebar.selectbox("Non-Linear Optimization",Non_linear_opti)
#
# if home_page:
#     home()
#
# #Option For S1
# if S1 == "Bisection Method":
#     bisection_method()
# if S1 == "False-Position Method":
#     false_position_method()
# elif S1 == "Secant Method":
#     secant_method()
# elif S1 == "Newton Method":
#     newton_method()
#
# #Option for S2
# if S2 == "Gaussian directed Elimination":
#     gaussian_directed_elimination()
# elif S2 == "Gaussian-Jordan directed Elimination":
#     gaussian_jordan_directed_elimination()
# elif S2 == "Gauss-Seidel iterative Method":
#     gauss_seidel_iterative_Method()
# elif S2 == "Jacobi iterative Method":
#     jacobi_iterative_method()
navigation = st.sidebar

homepage = option_menu(None,options = ["Home", "Root-Finding Methods", "Linear Algebraic Equations",'Numerical Differentiation','Numerical Integration','Non-Linear Optimization'],
    icons=['house','calculator', "braces",'list-ol','type-italic',"graph-up"],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container":{"width":"100%"},
        "nav-link": {"font-size": "12px", "text-align": "center", "margin":"0px","color":"#eee"},
        "nav-link-selected": {
            "background-color": "#112A46",
        }
    }
    )


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


