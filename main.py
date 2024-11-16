import streamlit as st


# Define the different pages as functions
def home():
    st.title("About ")
    st.write("")


def project1():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")


def project2():
    st.title("About Page")
    st.write("Learn more about this application here.")


def project3():
    st.title("Contact Page")
    st.write("Get in touch with us.")


def project4():
    st.title("Contact Page")
    st.write("Get in touch with us.")


def project5():
    st.title("Contact Page")
    st.write("Get in touch with us.")


def project6():
    st.title("Contact Page")
    st.write("Get in touch with us.")


def project7():
    st.title("Contact Page")
    st.write("Get in touch with us.")


def project8():
    st.title("Contact Page")
    st.write("Get in touch with us.")


def project9():
    st.title("Contact Page")
    st.write("Get in touch with us.")



page_names_to_funcs = {
    "Home": home,
    "Project 1": project1,
    "Project 2": project2,
    "Project 3": project3,
    "Project 4": project4,
    "Project 5": project5,
    "Project 6": project6,
    "Project 7": project7,
    "Project 8": project8,
    "Project 9": project9
}
root_finding_methods = {
    "Bisection Method",
    "False-Position Method",
    "Secant Method",
    "Newton Method"
}
linear_algebraic_methods = {
    "Gaussian directed Elimination",
    "Gaussian-Jordan directed Elimination",
    "Gauss-Seidel iterative Method",
    "Jacobi iterative Method",
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

pages = st.sidebar.button("Home",home())
S1 = st.sidebar.selectbox("Root-Finding Methods",root_finding_methods)
S2 = st.sidebar.selectbox("Numerical linear algebraic equations",linear_algebraic_methods)
S3 = st.sidebar.selectbox("Numerical Differentiation",Numerical_diff)
S4 = st.sidebar.selectbox("Numerical Integration",Numerical_int)
S5 = st.sidebar.selectbox("Non-Linear Optimization",Non_linear_opti)