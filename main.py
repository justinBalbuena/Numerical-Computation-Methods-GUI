import streamlit as st

from format_functions import *
from functions.justin.project7.lagrange_interpolation import lagrange_interpolation
from layout_for_project3 import run_page_3

st. set_page_config(layout="wide")

# Define the different pages as functions
def home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")


def project1():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")


def project2():
    st.title("About Page")
    st.write("Learn more about this application here.")


def project3():
    run_page_3()

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
    st.title("Lagrange Interpolation")

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
                <h4 class="text">Please enter how many set of values you would like to put</h4>
            </div>
        """,
        unsafe_allow_html=True
    )

    # Number of columns input
    columns = st.text_input(label="**:green[Columns]**: ", key="amount_of_columns")
    wanted_value = st.text_input(label="**:green[Wanted Value to Interpolate]**: ", key="users_wanted_value")
    # Only create fields if `columns` is a valid integer
    if columns and columns.isdigit() and wanted_value:
        columns = int(columns)
        st.session_state["columns"] = columns  # Save the columns count in session state

        wanted_value = float(wanted_value)
        st.session_state["wanted_value"] = wanted_value

        # Dynamically generate x and y input fields based on the number of columns
        x_y_field(columns)


        # Collect values in x and y arrays when the "Input Values" button is clicked
        if st.button("Input Values"):
            st.session_state["x_arr"] = [st.session_state.get(f"input_field_{i}", "") for i in range(1, columns + 1)]
            st.session_state["y_arr"] = [st.session_state.get(f"input_field_{i}", "") for i in range(columns + 1, 2 * columns + 1)]

            x_arr = [float(x) for x in st.session_state["x_arr"]]
            y_arr = [float(y) for y in st.session_state["y_arr"]]

            st.markdown(
                f"""
                    <style>
                    .focus_highlight {{
                        color: green;
                    }}
                    </style>
                    
                    <h4>
                        The interpolated value at <span class="focus_highlight">{st.session_state["wanted_value"]}</span> is: <span class="focus_highlight">{lagrange_interpolation(x_arr, y_arr, st.session_state["wanted_value"])}</span>
                    </h4>
                
                """,
                unsafe_allow_html=True
            )

def project8():
    st.title("Contact Page")
    st.write("Get in touch with us.")


def project9():
    st.title("Contact Page")
    st.write("Get in touch with us.")


def project10():
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
    "Project 9": project9,
    "Project 10": project10
}
pages = st.sidebar.selectbox("Choose a project", page_names_to_funcs.keys())
page_names_to_funcs[pages]()
