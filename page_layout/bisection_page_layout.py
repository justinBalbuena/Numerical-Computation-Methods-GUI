import streamlit as st
from page_layout.error_option import error_tolerance_methods
from project_function.bisection_method import ant_bisection_method,find_roots
from page_layout.convert_mathexpression import transform_math_expression
def bisection_page_layout():
    st.title("Bisection Method")
    #Explain the Theorem
    st.header("Theorem",divider="blue")
    st.write("An equation f(x)=0, where f(x) is a real continuous function, has at least one root between x1 and x2 if f(x1) f(x2) < 0 (the function changes sign on opposite sides of the root)")
    st.write("So at least one root of the equation f(x)=0 exists between the two points if the function f(x) is real, continuous, and changes sign on the interval [x1,x2]")
    #this is calculation section
    st.header("Calculation",divider="blue")

    #Calculation Section
    bisection_form = st.form(key="bisection_form")
    error_method = bisection_form.radio("Error Tolerance Method",error_tolerance_methods.keys())
    #value of the flag
    flag = error_tolerance_methods[error_method]()
    #user input for function
    function = bisection_form.text_input("Enter a function Ex. 2sin(x)-e^x/4-1")
    #value for x1
    x1 = bisection_form.number_input(label="Enter a value for x1",value=None,format="%f")
    #value for x2
    x2 = bisection_form.number_input(label="Enter a value for x2",value=None,format="%f")
    #tolerance
    tolerance = bisection_form.number_input(label="Tolerance value (no negative)",value=None,format="%f",min_value=0.0000000000000000001)
    #button to execute the script
    pressed = bisection_form.form_submit_button("Evaluate")

    #Result Section
    if pressed:
        st.header("Results",divider="blue")
        function= transform_math_expression(function)
        root = ant_bisection_method(x1,x2,function,tolerance,flag)
        true_root = find_roots(function,(x2+x1)/2)
        if root:
            st.write("The Root of the function ",function," is: ",root)
            st.write("True Value: ",true_root)
            st.write("")
        else:
            st.write("The Root for the function could not be found!")
