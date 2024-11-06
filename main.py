import streamlit as st
import functions

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
    st.title("Lagrange Interpolation")

    st.html(
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
        """
    )
    st.text_input(label="**:green[Input]**: ", key="amount_of_values")


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
pages = st.sidebar.selectbox("Choose a project", page_names_to_funcs.keys())
page_names_to_funcs[pages]()
