import sys
import streamlit as st
from streamlit_option_menu import option_menu
#must download streamlit option menu
st.set_page_config(layout="wide")
# Define the different pages as functions
def home():
    st.title("Overview")
    st.write("Welcome! This is a simple GUI (Graphic User Interface) that preforms varies types of numerical methods. Done to ")
    sys.exit()
#
# def project1():
#     st.title("Home Page")
#     st.write("Welcome to the Home Page!")
#
#
# def project2():
#     st.title("About Page")
#     st.write("Learn more about this application here.")
#
#
# def project3():
#     st.title("Contact Page")
#     st.write("Get in touch with us.")
#
#
# def project4():
#     st.title("Contact Page")
#     st.write("Get in touch with us.")
#
#
# def project5():
#     st.title("Contact Page")
#     st.write("Get in touch with us.")
#
#
# def project6():
#     st.title("Contact Page")
#     st.write("Get in touch with us.")
#
#
# def project7():
#     st.title("Contact Page")
#     st.write("Get in touch with us.")
#
#
# def project8():
#     st.title("Contact Page")
#     st.write("Get in touch with us.")
#
#
# def project9():
#     st.title("Contact Page")
#     st.write("Get in touch with us.")

def bisection_method():
    st.title("Bisection Method")
def false_position_method():
    st.title("False Position Method")
def secant_method():
    st.title("Secant Method")
def newton_method():
    st.title("Newton Method")

def gaussian_directed_elimination():
    st.title("Gaussian Directed Elimination")
def gaussian_jordan_directed_elimination():
    st.title("Gaussian Jordan Directed Elimination")
def gauss_seidel_iterative_Method():
    st.title("Gaussian Seidel Iterative Method")
def jacobi_iterative_method():
    st.title("Jacobi Iterative Method")


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
    "Lagrange Interpolation",
    "Two point forward difference formula",
    "Three point center difference formula",
    "Three point forward difference formula",
}
Numerical_int = {
    "Trapezoidal rule (multiple application)",
    "Simpson's rule (Composite)"
}
Non_linear_opti = {
    "Golden Section Method",
    "Newton Method"
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
