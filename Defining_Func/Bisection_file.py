import streamlit as st
from sympy import *
from functions.Shirley.Project_1.Bisection_method import bisection_method

def Project1():
    global original_function
    st.title("Bisection method")
    st.markdown(
        f"""
                <style>
                    .size_box {{
                        justify-content: center;
                        align-items: center;
                    }}
                    .text {{
                        padding-top: 16px;
                        padding-bottom: 16px;
                    }}
                </style>
                <div class="size_box">
                    <h4 class="text">Please enter the following values</h4>
                </div>
            """,
        unsafe_allow_html=True
    )
    inputx1 = st.text_input(label="**:blue[Input for x1: ]**")
    inputx2 = st.text_input(label="**:blue[Input for x2: ]**")
    user_tolerance = st.text_input(label="**:blue[Input for tolerance: ]**")
    st.write(":blue[Please choose a flag: ]")
    user_flag = st.selectbox(label="**:blue[a = absolute approximate error;\nb = absolute relative approximate error;\nc = estimated true absolute error;\nd = both the absolute approximate and estimated true absolute error;]**", options=['a', 'b', 'c', 'd'])
    user_function = st.text_input(label="**:blue[Input for the function \n{ Example: 4 * sin(x)-(sqrt(x))+log(2*x) }\n: ]**")
    if st.button("Bisection Method"):
        if inputx1 and inputx2 and user_tolerance and user_flag and user_function:
            x1 = float(inputx1)
            x2 = float(inputx2)
            tolerance = float(user_tolerance)
            flag = str(user_flag)
            x = symbols('x')  # x is an unknown value
            try:
                parsed_function = sympify(user_function)
                original_function = lambdify(x, parsed_function)  # taking in the user function as a lambda function
            except SympifyError as e:
                print(f"Invalid function: {user_function}. Error: {e}")
                original_function = None
            result = bisection_method(x1,x2,tolerance,flag,original_function) #setting result equal to bisection function by
            print(result)
            st.markdown(
                f"""
                    <style>
                    .focus_highlight {{
                        color: green;
                    }}
                    </style>
    
                    <h4>
                    The result of the Bisection Method is:
                    <span class="focus_highlight">{result}</span>
    
                """,
            unsafe_allow_html=True
            )
    else:
        st.error("Please provide valid inputs for all fields.")
